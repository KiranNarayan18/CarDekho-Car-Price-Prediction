from src.custom_logger import logger
from src.config import ConfigurationManager
from src.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass    

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
           
            logger.info(f"data ingestion successful")

        except Exception as error:
            logger.error(f"error downloading data: {error}")
            