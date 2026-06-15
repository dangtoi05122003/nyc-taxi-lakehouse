import os
from dotenv import load_dotenv
from dataclasses import dataclass
@dataclass
class setting:
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    BUCKET_NAME: str
    TRINO_ENDPOINT: str
    TRINO_PORT: int
    TRINO_USER: str
    TRINO_CATALOG: str
    TRINO_SCHEMA: str
def load_setting()-> setting:
    load_dotenv()
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
    BUCKET_NAME = os.getenv("BUCKET_NAME")
    TRINO_ENDPOINT = os.getenv("TRINO_ENDPOINT")
    TRINO_PORT = int(os.getenv("TRINO_PORT"))
    TRINO_USER = os.getenv("TRINO_USER")
    TRINO_CATALOG = os.getenv("TRINO_CATALOG")
    TRINO_SCHEMA = os.getenv("TRINO_SCHEMA")
    return setting(MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, BUCKET_NAME, TRINO_ENDPOINT, TRINO_PORT, TRINO_USER, TRINO_CATALOG, TRINO_SCHEMA)