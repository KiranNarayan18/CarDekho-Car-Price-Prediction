import os
from src.constants import *
from src.utils.common import read_yaml
from src.custom_logger import logger

from src.entity import DataIngestionConfig

class ConfigurationManager:

    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):

        self.config = read_yaml(config_filepath)
        
        os.makedirs(self.config.artifacts_root, exist_ok=True)

    def get_data_ingestion_config(self):
        try:
            
            config = self.config.data_ingestion

            os.makedirs(config.root_dir, exist_ok=True)

            data_ingestion_config = DataIngestionConfig(
                root_dir = config.root_dir,
                source_url = config.source_url
            )

            return data_ingestion_config


        except Exception as error:
            logger.error(f"error while reading configuration: {error}")