from catalog.schema import Schema

class Nyc(Schema):
    def __init__(self, config_path, format):
        super().__init__(config_path, format)

if __name__ == "__main__":
    app = Nyc("/opt/airflow/config/schema/nyc.yml", 'PARQUET')
    app.create_all_tables()