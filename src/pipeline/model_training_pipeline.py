
from src.custom_logger import logger
from src.config.configuration import ConfigurationManager
from src.components.model_training import ModelTraininer


class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            obj = ConfigurationManager()
            obj = obj.get_model_training_config()

            obj1 = ModelTraininer(obj)
            obj1.initiate_model_training()

        except Exception as error:
            logger.error(f"Error creating model: {error}")



if __name__ == '__main__':
    obj = ModelTrainingPipeline()
    obj.main()
    