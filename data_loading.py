import numpy as np
import pandas as pd
VERBOSE = False

class DataLoader:
    def __init__(self):
        ...

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv('space_missions_dataset.csv')



if __name__ == '__main__':
    loader = DataLoader()
    data = loader.load_data()


