from data_loading import DataLoader
import matplotlib.pyplot as plt
import parameters as params
import seaborn as sns
VERBOSE = True




class DataPlotter:
    def __init__(self, loader: DataLoader):
        self.data = None
        self.loader = loader
        self.load_data()

    def load_data(self):
        self.data = self.loader.load_data()

    def mission_name(self,column_name:str) -> None:
        sns.scatterplot(data=self.data, x='Mission_Name', y=column_name)
        plt.xticks(rotation=45, fontsize=7)
        plt.show()

    def distance_by_fuel_consumption(self):
        sns.relplot(data=self.data, x=params.DISTANCE_FROM_EARTH, y=params.FUEL_CONSUMPTION, hue=params.M_SUCCESS)
        plt.xticks(rotation=45, fontsize=7)
        plt.show()


    def success_by_scientific_y(self):
        sns.relplot(data=self.data, x=params.SCIENTIFIC_YIELD, y=params.M_SUCCESS, hue=params.CREW)
        plt.xticks(rotation=45, fontsize=7)
        plt.show()

    def success_by_mission_cost(self):
        # sns.relplot(data=self.data, x=params.COST, y=params.M_SUCCESS, hue=params.MISSION_TYPE)
        # sns.regplot(data=self.data, x=params.COST, y=params.M_SUCCESS)
        sns.kdeplot(
            data=self.data,
            x='Mission_Cost_billion_USD',
            y='Mission_Success_percent',
            cmap='Blues', fill=True
        )
        plt.xticks(rotation=45, fontsize=7)
        plt.show()



if __name__ == '__main__':
    plotter = DataPlotter(loader=DataLoader())
    # plotter.mission_name(params.M_SUCCESS)
    plotter.distance_by_fuel_consumption()
    # plotter.success_by_scientific_y()
    # plotter.success_by_mission_cost()
