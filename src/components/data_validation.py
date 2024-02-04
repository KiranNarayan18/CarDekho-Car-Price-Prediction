"""
Author: Kiran Narayan
version: v1.0
Data: 01-02-2024
"""

## components
import glob
import pandas as pd
import os

from src.custom_logger import logger
from src.entity import DataValidationConfig

class DataValidator:
    def __init__(self, config: DataValidationConfig):
        self.config = config        
        self.data_filepath = glob.glob(os.path.join(self.config.root_dir, '*.csv'))[0]        

    def initiate_validation(self):
        try:
            
            df = pd.read_csv(self.data_filepath)            
            col_names = self.config.schema.keys()

            df['NoOfYears']=2024 - df['Year']


            df.drop(self.config.columns_to_drop.name, axis=1, inplace=True)

            ##checking for number of columns
            if len(df.columns) != len(col_names):
                logger.info(f"invalid number of columns")
                return 
                
            ## checking for data types of the column
            if not (all([df[col].dtype == dtype for col, dtype in self.config.schema.items()])):
                logger.info(f"invalid datatype for the columns")
                return 
            
            ## checking for null values in the dataframe
            if not all(df.isna()):
                logger.info(f"there are missing values in the dataframe")
                logger.info(f"please handle the missing values before proceeding")

            
            os.makedirs(self.config.clean_dir, exist_ok=True)

            df.to_csv(f'{self.config.clean_dir}//cleaned_data.csv', index=False)
            
        except Exception as error:
            logger.error(f"error while validating data: {error}")


if __name__ == '__main__':
    from src.config.configuration import ConfigurationManager

    obj = ConfigurationManager()
    res = obj.get_data_validation_config()

    obj2 = DataValidator(res)
    obj2.initiate_validation()