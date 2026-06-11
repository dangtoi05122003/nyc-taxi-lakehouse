from pyspark.sql import SparkSession
from .Setting import load_setting
setting = load_setting()
def get_spark(endpoint = setting.MINIO_ENDPOINT):
    return SparkSession.builder.appName(setting.BUCKET_NAME) \
        .master("local[*]") \
        .config("spark.driver.memory", "12g") \
        .config("spark.executor.memory", "12g") \
        .config("spark.memory.offHeap.size", "4g") \
        .config("spark.memory.offHeap.enabled", "true") \
        .config("spark.hadoop.fs.s3a.fast.upload", "true") \
        .config("spark.hadoop.fs.s3a.fast.upload.buffer", "disk") \
        .config("spark.hadoop.fs.s3a.endpoint", f"{endpoint}") \
        .config("spark.hadoop.fs.s3a.access.key", f"{setting.MINIO_ACCESS_KEY}") \
        .config("spark.hadoop.fs.s3a.secret.key", f"{setting.MINIO_SECRET_KEY}") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
        .getOrCreate()
