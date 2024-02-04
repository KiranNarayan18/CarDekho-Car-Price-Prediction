import joblib 
import numpy as np
import pandas as pd
from pathlib import Path


from src.custom_logger import logger

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/models/random_forest_regression_model.pkl'))
        
    
    def predict_output(self, data):

        try:

            data["NoOfYears"] = 2024 - data['Year']

            data['Seller_Type_Individual'] = False
            if data['Seller_Type'] == 'Individual':
                data['Seller_Type_Individual'] = True


            data['Transmission_Manual'] = False
            if data['Transmission'] == 'Manual':
                data['Transmission_Manual'] = True


            data['Fuel_Type_Diesel'] = False
            data['Fuel_Type_Petrol'] = False

            if data['Fuel_Type'] == 'Petrol':
                data['Fuel_Type_Petrol'] = True

            elif data['Fuel_Type'] == 'Diesel':
                data['Fuel_Type_Diesel'] = True

            columns = ["Present_Price", "Kms_Driven",	"Owner", "NoOfYears",	"Fuel_Type_Diesel",	"Fuel_Type_Petrol",	"Seller_Type_Individual", "Transmission_Manual"]

            #convert to dataframe
            df = pd.DataFrame([data])
            df.set_index('Car_Name', inplace=True)
            df = df[columns]

            prediction = self.model.predict(df)

            return round(prediction[0], 2)
        
        except Exception as error:
            logger.error(f"error in prediction pipeline: {error}")




if __name__ == '__main__':


    data = {"Car_Name": "ritz",
        "Year": 2014,        
        "Present_Price": 5.59,
        "Kms_Driven": 27000,
        "Fuel_Type": "Petrol",
        "Seller_Type": "Dealer",
        "Transmission": "Manual",
        "Owner": 0}
            

    obj = PredictionPipeline()
    prediction = obj.predict_output(data)
    print(prediction)