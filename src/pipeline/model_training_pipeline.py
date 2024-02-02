
from src.custom_logger import logger
from src.config.configuration import ConfigurationManager
from src.components.model_training import ModelTraininer


if __name__ == '__main__':

    obj = ConfigurationManager()
    obj = obj.get_model_training_config()

    obj1 = ModelTraininer(obj)
    obj1.initiate_model_training()