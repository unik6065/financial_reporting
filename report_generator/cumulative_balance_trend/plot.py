import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class CumulativeBalanceTrend():

    def printGraph(self, dataFrame: pd.DataFrame):

        graphPath = './hello/graphs/CumulativeBalanceTrend.png'
        displayPath = './graphs/CumulativeBalanceTrend.png'

        x = dataFrame['Date']
        y = dataFrame['Solde']

        plt.style.use('_mpl-gallery')
        plt.subplots_adjust(left=0.2,bottom=0.2, top = 0.9, right = 0.9)

        fig, ax = plt.subplots()

        ax.set_xlabel('Date')
        ax.set_ylabel('Balance')


        fig.set_size_inches(10,6)
        ax.plot(x, y)
        plt.savefig(graphPath)

        return displayPath
