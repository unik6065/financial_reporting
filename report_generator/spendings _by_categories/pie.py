import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class SpendingByCategoriesPie():

    def printGraph(self, dataFrame: pd.DataFrame):
        graphPath = './hello/graphs/SpendingsByCategories.png'
        displayPath = './graphs/SpendingsByCategories.png'

        fig, ax = plt.subplots()
        fig.set_size_inches(10,6)
        ax.pie(abs(dataFrame), labels=dataFrame.index, autopct='%1.1f%%')

        plt.savefig(graphPath)

        return displayPath
