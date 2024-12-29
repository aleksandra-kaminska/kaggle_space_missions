from data_loading import DataLoader
import numpy as np
import pandas as pd
import parameters as params
import statsmodels.formula.api as smodels

class Model:
    def __init__(self, loader: DataLoader):
        self.data = None
        self.loader = loader
        self._load_data()

    def _load_data(self):
        self.data = self.loader.load_data()

    def linear_regression(self):
        self.data[params.MISSION_TYPE] = self.data[params.MISSION_TYPE].astype('category')
        self.data[params.TARGET_TYPE] = self.data[params.TARGET_TYPE].astype('category')
        model = smodels.ols(
            formula = 'Mission_Success_percent ~ Target_Type + Mission_Type + '
                      'Distance_from_Earth_light_years + Mission_Duration_years +'
                      ' Crew_Size + Mission_Cost_billion_USD + Fuel_Consumption_tons +'
                      ' Payload_Weight_tons + Scientific_Yield_points',
            data = self.data
        ).fit()
        print(model.summary())

if __name__ == '__main__':
    model = Model(DataLoader())
    if model.data is not None:
        print('Linear regression results:')
        model.linear_regression()




