from minio import Minio
from minio.error import S3Error
from utils import load_setting, get_logger

setting = load_setting()
logger = get_logger(__name__)
class minioService:
    def __init__(self):
        self.client = Minio(
            setting.MINIO_ENDPOINT,
            access_key=setting.MINIO_ACCESS_KEY,
            secret_key=setting.MINIO_SECRET_KEY,
            secure=False
        )
        self.create_bucket(setting.BUCKET_NAME)
    def create_bucket(self, bucket_name: str):
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
                logger.info(f"Bucket: '{bucket_name}' đã được tạo thành công.")
        except S3Error as e:
            logger.error(f"Lỗi khi tạo bucket: {e}")
    def put_object(self, bucket_name, object_name, data, length, content_type="application/octet-stream"):
        try:
            self.client.put_object(
                bucket_name,
                object_name,
                data,
                length=length,
                content_type=content_type
            )
        except Exception as e:
            logger.error("Upload failed: %s", e)
            raise