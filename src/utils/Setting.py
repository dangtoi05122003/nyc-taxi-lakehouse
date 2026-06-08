import os
from dotenv import load_dotenv
from dataclasses import dataclass
@dataclass
class setting:
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    BUCKET_NAME: str
def load_setting()-> setting:
    load_dotenv()
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
    BUCKET_NAME = os.getenv("BUCKET_NAME")
    return setting(MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, BUCKET_NAME)