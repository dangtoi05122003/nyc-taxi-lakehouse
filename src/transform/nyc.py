from utils import get_logger, load_yaml
from utils.spark_session import get_spark
import pyspark.sql.functions as F
logger = get_logger(__name__)

class nyc:
    def __init__(self, config_path):
        self.config = load_yaml(config_path)
        self.spark = get_spark()
    def process(self, df, process):
        for step in process:
            if "refinement" in step:
                refinement = step["refinement"]
                if "drop_columns" in refinement:
                    for col in refinement["drop_columns"]:
                        df = df.drop(col)
                if "filters" in refinement:
                    df = df.filter(F.expr(refinement["filters"]))
            if "calculations" in step:
                for col, cal in step['calculations'].items():
                    df = df.withColumn(col, F.expr(cal))
        return df
    def run(self):
        tables = self.config['tables']
        basePath = self.config['path']['basePath']
        for table_name, table_config in tables.items():
            logger.info(f"Chuẩn bị xử lý {table_name}")
            process = table_config['process']
            df = self.spark.read.option("basePath", basePath).option("pathGlobFilter", f"{table_name}_*.parquet").parquet(f"{basePath}year=*/month=*/")
            df = self.process(df, process)
            df.repartition(100).write.mode("overwrite").partitionBy("year", "month").parquet(f"{self.config['path']['outputPath']}/{table_name}")
if __name__ == "__main__":
    app =nyc(config_path="/opt/spark/config/silver/nyc.yml")
    app.run()