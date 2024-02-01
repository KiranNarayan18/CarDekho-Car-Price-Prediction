import os
import pandas as pd
from sklearn.model_selection import train_test_split


from src.entity import DataTransformationConfig
from src.custom_logger import logger

class DataTransfomer:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        print(self.config)


    def initiate_transfomation(self):
        
        try:
            
            df = pd.read_csv(os.path.join(self.config.root_dir, 'cleaned_data.csv'), index_col=0)

            df = pd.get_dummies(df,drop_first=True)

            train_df, test_df = train_test_split(df, test_size=0.3, random_state=0)

            train_df.to_csv(os.path.join(self.config.transformed_dir, 'train.csv'))
            test_df.to_csv(os.path.join(self.config.transformed_dir, 'test.csv'))
            

        except Exception as error:
            logger.error(f"error in data transformation: {error}")