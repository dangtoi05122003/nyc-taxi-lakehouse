from trino.dbapi import connect
from utils import load_setting, get_logger

logger = get_logger(__name__)
setting = load_setting()
class TrinoClient:
    def __init__(self):
        self.cur = self.get_trino_cursor()
    def get_trino_cursor(self):
        conn = connect(
            host=setting.TRINO_ENDPOINT,
            port=setting.TRINO_PORT,
            user=setting.TRINO_USER,
            catalog=setting.TRINO_CATALOG,
            schema=setting.TRINO_SCHEMA,
        )
        logger.info("Trino connected")
        return conn.cursor()
    def create_table(self, tablename, columns, partition_by, path, format):
        logger.info(f"Creating table: {tablename}")
        try:
            location = f"{path}/{tablename}"
            column = ",\n".join([f"{col} {dtype}" for col, dtype in columns.items()])
            partition = ", ".join([f"'{p}'" for p in partition_by])
            options = ""
            if format.lower() == "csv":
                options = ", skip_header_line_count = 1"
            self.cur.execute(f"""
                CREATE TABLE IF NOT EXISTS {setting.TRINO_CATALOG}.{setting.TRINO_SCHEMA}.{tablename} (
                    {column}
                )
                WITH (
                    external_location = '{location}',
                    format = '{format}',
                    partitioned_by = ARRAY[{partition}]
                    {options}
                )
            """)
            logger.info(f"Table {setting.TRINO_SCHEMA}.{tablename} is ready")
            if partition_by:
                self.sync_partitions(tablename)
        except Exception:
            logger.exception(f"Failed to create table {tablename}")
            raise
    def sync_partitions(self, tablename):
        try:
            self.cur.execute(f"""
                CALL system.sync_partition_metadata(
                    schema_name => '{setting.TRINO_SCHEMA}',
                    table_name => '{tablename}',
                    mode => 'ADD'
                )
            """)
        except Exception:
            logger.exception(f"Failed to sync partitions: {tablename}")
            raise
    def drop_table(self, tablename):
        logger.info(f"Dropping table: {tablename}")
        try:
            self.cur.execute(f"""
                DROP TABLE IF EXISTS {setting.TRINO_SCHEMA}.{tablename}
            """)
        except Exception:
            logger.exception(f"Failed to drop table: {tablename}")
            raise