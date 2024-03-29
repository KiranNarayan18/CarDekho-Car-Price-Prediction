"""
Author: Kiran Narayan
version: v1.0
Data: 01-02-2024
"""

import os
from src.constants import *
from src.utils.common import read_yaml
from src.custom_logger import logger

from src.entity import (DataIngestionConfig,
                        DataValidationConfig,
                        DataTransformationConfig,
                        ModelTrainingConfig)

class ConfigurationManager:

    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        schema_filepath =  SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)        
        os.makedirs(self.config.artifacts_root, exist_ok=True)

        self.schema_config = read_yaml(schema_filepath)    
        

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



    def get_data_validation_config(self):
        try:
            
            config = self.config.data_validation

            os.makedirs(config.root_dir, exist_ok=True)

            columns = dict(self.schema_config.COLUMNS)


            data_validation_config = DataValidationConfig(
               root_dir = config.root_dir,
               clean_dir = config.clean_dir,
               schema = columns,
               target_column= self.schema_config.TARGET_COLUMN,
               columns_to_drop=self.schema_config.COLUMNS_TO_DROP
            )

            return data_validation_config

        except Exception as error:
            logger.error(f"error while reading configuration: {error}")


    

    def get_data_transformation_config(self):
        try:
            config = self.config.data_transformation

            os.makedirs(config.transformed_dir, exist_ok=True)

            data_transformation_config = DataTransformationConfig(
                root_dir = config.root_dir,
                transformed_dir=config.transformed_dir,
                target_column= self.schema_config.TARGET_COLUMN,
            )

            return data_transformation_config

        except Exception as error:
            logger.error(f"error while getting data transformation: {error}")


    
    def get_model_training_config(self):
        try:
            
            config = self.config.model_training

            os.makedirs(config.model_dir, exist_ok=True)
            
            data_ingestion_config = ModelTrainingConfig(
                root_dir = config.root_dir,
                model_dir = config.model_dir,
                target_column = self.schema_config.TARGET_COLUMN.name,
            )

            return data_ingestion_config


        except Exception as error:
            logger.error(f"error while reading configuration: {error}")