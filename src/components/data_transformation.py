"""
Author: Kiran Narayan
version: v1.0
Data: 01-02-2024
"""


import os
import pandas as pd
from sklearn.model_selection import train_test_split


from src.entity import DataTransformationConfig
from src.custom_logger import logger

class DataTransfomer:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        
    def initiate_transfomation(self):
        
        try:
            
            df = pd.read_csv(os.path.join(self.config.root_dir, 'cleaned_data.csv'), index_col=0)

            df = pd.get_dummies(df,drop_first=True)

            train_df, test_df = train_test_split(df, test_size=0.3, random_state=0)

            train_df.to_csv(os.path.join(self.config.transformed_dir, 'train.csv'), index=False)
            test_df.to_csv(os.path.join(self.config.transformed_dir, 'test.csv'), index=False)
            

        except Exception as error:
            logger.error(f"error in data transformation: {error}")


if __name__ == '__main__':

    from src.config.configuration import ConfigurationManager

    obj1 = ConfigurationManager()
    obj1 = obj1.get_data_transformation_config()

    obj = DataTransfomer(obj1)
    obj.initiate_transfomation()