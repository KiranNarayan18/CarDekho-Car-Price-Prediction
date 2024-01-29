import os
import glob
import pandas as pd

from src.custom_logger import logger
from src.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config        
        self.data_filepath = glob.glob(os.path.join(self.config.root_dir, '*.csv'))[0]
        
    def initiate_validation(self):
        try:
            
            df = pd.read_csv(self.data_filepath)            
            col_names = self.config.schema.keys()

            df.drop(self.config.columns_to_drop, inplace=True)

            if len(df.columns) != len(col_names):
                print(f"invalid number of columns")
                
                print([i for i in df.columns if i not in col_names])

                print(len(df.columns), len(col_names))
            
            
        except Exception as error:
            logger.error(f"error while validating data: {error}")