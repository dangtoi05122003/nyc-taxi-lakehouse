from Service import minioService
from utils import load_yaml, get_logger, load_setting
import requests
import re
from io import BytesIO
from bs4 import BeautifulSoup
logger = get_logger(__name__)
setting =load_setting()
class bronze:
    def __init__(self, config_path):
        self.config = load_yaml(config_path)
        self.client =minioService()
        self.connect()
    def connect(self):
        response = requests.get(self.config['nyc']['base-url'], headers={"User-Agent": "Mozilla/5.0"})
        self.soup = BeautifulSoup(response.text, "html.parser")
    def get_data(self) -> list[str]:
        links = []
        for a in self.soup.find_all('a'):
            href = (a.get('href')).strip()
            if "parquet" in href.lower():
                links.append(href)
        logger.info(links)
        return links
    def extract_year_month(self, url):
        match = re.search(r"(\d{4})-(\d{2})", url)
        if not match:
            return None, None
        return int(match.group(1)), match.group(2)
    def ingest(self):
        for file_url in self.get_data():
            year, month = self.extract_year_month(file_url)
            if not year or year < 2024:
                continue
            file_name = file_url.split("/")[-1]
            bronze_path = f"bronze/year={year}/month={month}/{file_name}"
            logger.info(f"Processing: {bronze_path}")
            try:
                res = requests.get(file_url, stream=True, headers={"User-Agent": "Mozilla/5.0"})
                res.raise_for_status()
                data = BytesIO(res.content)
                self.client.put_object(
                    setting.BUCKET_NAME,
                    bronze_path,
                    data,
                    length=len(res.content),
                    content_type="application/octet-stream"
                )
                logger.info("Uploaded: %s", bronze_path)
            except Exception as e:
                logger.error("Error file %s: %s", file_name, e)
if __name__ == "__main__":
    app = bronze(config_path="/opt/airflow/config/bronze.yml")
    app.ingest()