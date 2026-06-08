import yaml
from pathlib import Path
from .logger import get_logger

logger = get_logger(__name__)
def load_yaml(path: Path):
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f)
            logger.info(f"Đọc file cấu hình thành công với {path}")
            return config
    except Exception as e:
        logger.error(f"Lỗi khi tải file cấu hình tại {path}: {e}")
        raise