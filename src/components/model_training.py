## components

import os
import pickle
import numpy as np
import pandas as pd
from sklearn import metrics

from src.custom_logger import logger
from src.entity import ModelTrainingConfig
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV


class ModelTraininer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    def initiate_model_training(self):
        try:

            train_df = pd.read_csv(os.path.join(self.config.root_dir, 'train.csv'))
            test_df = pd.read_csv(os.path.join(self.config.root_dir, 'test.csv'))

            X_train = train_df.drop(self.config.target_column, axis=1)
            y_train = train_df[self.config.target_column]

            X_test = test_df.drop(self.config.target_column, axis=1)
            y_test = test_df[self.config.target_column]

            n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
            # Number of features to consider at every split
            max_features = ['sqrt', 'log2', None]
            # Maximum number of levels in tree
            max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]
            # max_depth.append(None)
            # Minimum number of samples required to split a node
            min_samples_split = [2, 5, 10, 15, 100]
            # Minimum number of samples required at each leaf node
            min_samples_leaf = [1, 2, 5, 10]

            random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}
            
            rf = RandomForestRegressor()

            rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid,scoring='neg_mean_squared_error', n_iter = 10, cv = 5, verbose=2, random_state=42, n_jobs = 1)

            rf_random.fit(X_train,y_train)

            print(rf_random.best_params_)

            print(rf_random.best_score_)

            predictions=rf_random.predict(X_test)

            print('MAE:', metrics.mean_absolute_error(y_test, predictions))
            print('MSE:', metrics.mean_squared_error(y_test, predictions))
            print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

            file = open(os.path.join(self.config.model_dir, 'random_forest_regression_model.pkl'), 'wb')
            pickle.dump(rf_random, file)

        except Exception as error:
            logger.error(f" error found while training: {error}")






if __name__ == '__main__':

    from src.config.configuration import ConfigurationManager

    obj = ConfigurationManager()
    obj = obj.get_model_training_config()

    obj1 = ModelTraininer(obj)
    obj1.initiate_model_training()