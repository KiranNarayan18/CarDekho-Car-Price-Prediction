"""
Author: Kiran Narayan
version: v1.0
Data: 01-02-2024
"""


from src.custom_logger import logger
from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidator

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            obj = ConfigurationManager()
            res = obj.get_data_validation_config()

            obj2 = DataValidator(res)
            obj2.initiate_validation()

        except Exception as error:
            logger.error(f"Failed to validate data: {error}")


if __name__ == '__main__':
    obj = DataValidationPipeline()
    obj.main()

    