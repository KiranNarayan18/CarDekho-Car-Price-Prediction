import os
from urllib import request
from src.custom_logger import logger
from src.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):        
        try:
            os.makedirs(self.config.root_dir, exist_ok=True)
            self.filename = os.path.basename(self.config.source_url)
            request.urlretrieve(self.config.source_url, os.path.join(self.config.root_dir, self.filename))

        except Exception as error:
            logger.error(f'Error downloading data: {error}')
