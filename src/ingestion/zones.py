from Service import minioService
from utils import load_yaml, get_logger, load_setting
import pandas as pd
from io import BytesIO
logger = get_logger(__name__)
setting = load_setting()

class zones:
    def __init__(self, config_path):
        self.config = load_yaml(config_path)['zones']
        self.client = minioService()
    def fetch_data(self):
        try:
            df = pd.read_csv(self.config['base-url'])
            logger.info(f"Tải thành công {len(df)}")
            return df
        except Exception as e:
            logger.error(f"Lỗi khi tải dữ liệu từ URL: {str(e)}")
            raise e
    def ingest(self):
        try:
            df = self.fetch_data()
            df = df.to_csv(index=False).encode('utf-8')
            data = BytesIO(df)
            bronze_path = f"bronze/zones/taxi_zone_lookup.csv"
            self.client.put_object(
                setting.BUCKET_NAME,
                bronze_path,
                data,
                length=len(df),
                content_type="text/csv"
            )
            logger.info("Nạp dữ liệu zones lên tầng minio hoàn tất")
        except Exception as e:
            logger.error(f"Xử lý zones thất bại: {str(e)}")
            raise e
if __name__ == "__main__":
    app = zones(config_path="/opt/airflow/config/bronze.yml")
    app.ingest()