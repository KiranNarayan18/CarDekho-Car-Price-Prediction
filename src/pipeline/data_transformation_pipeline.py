
from src.custom_logger import logger
from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransfomer


class DataTransfomerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:

            obj1 = ConfigurationManager()
            obj1 = obj1.get_data_transformation_config()

            obj = DataTransfomer(obj1)
            obj.initiate_transfomation()

        except Exception as error:
            logger.error(f"error in DataTransfomer Pipeline: {error}")


if __name__ == "__main__":
    obj = DataTransfomerPipeline()
    obj.main()