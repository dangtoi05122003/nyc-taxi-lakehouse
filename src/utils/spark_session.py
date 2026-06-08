from pyspark.sql import SparkSession
from .Setting import load_setting
setting = load_setting()
def get_spark(endpoint = setting.MINIO_ENDPOINT):
    return SparkSession.builder.appName(setting.BUCKET_NAME) \
        .master("local[*]") \
        .config("spark.hadoop.fs.s3a.endpoint", f"{endpoint}") \
        .config("spark.hadoop.fs.s3a.access.key", f"{setting.MINIO_ACCESS_KEY}") \
        .config("spark.hadoop.fs.s3a.secret.key", f"{setting.MINIO_SECRET_KEY}") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262") \
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
        .getOrCreate()
