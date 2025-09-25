import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class TopMonthSpendingsPie():

    def printGraph(self, dataFrame: pd.DataFrame):
        x = abs(dataFrame['Montant'])
        labels = [1,2,3,4,5]
        graphPath = './hello/graphs/TopMonthSpendingsPie.png'
        displayPath = './graphs/TopMonthSpendingsPie.png'

        plt.style.use('_mpl-gallery-nogrid')
        colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

        fig, ax = plt.subplots()
        fig.set_size_inches(10,6)
        ax.pie(x, labels=labels, autopct='%1.1f%%')

        plt.savefig(graphPath)

        return displayPath
