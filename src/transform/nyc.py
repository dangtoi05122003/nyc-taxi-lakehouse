from utils import get_logger, load_yaml
from utils.spark_session import get_spark
import pyspark.sql.functions as F
from functools import reduce
from typing import List
logger = get_logger(__name__)

class nyc:
    def __init__(self, config_path):
        self.config = load_yaml(config_path)
        self.spark = get_spark()
    def process(self, df, process):
        for step in process:
            if "refinement" in step:
                refinement = step["refinement"]
                drop_columns = refinement.get("drop_columns", [])
                if drop_columns:
                    df = df.drop(*drop_columns)
                condition = self.build_filter_condition(refinement["filters"])
                if condition is not None:
                    df = df.filter(condition)
            if "calculations" in step:
                for col, cal in step['calculations'].items():
                    df = df.withColumn(col, F.expr(cal))
        return df
    def build_filter_condition(self, filters: List[str]):
        if not filters:
            return None
        conditions = map(F.expr, filters)
        return reduce(lambda left, right: left & right, conditions)
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