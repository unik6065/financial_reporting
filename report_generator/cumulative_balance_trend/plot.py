import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class CumulativeBalanceTrend():

    def printGraph(self, dataFrame: pd.DataFrame):

        graphPath = './hello/graphs/CumulativeBalanceTrend.png'
        displayPath = './graphs/CumulativeBalanceTrend.png'

        data = dataFrame.copy()
        data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, format="mixed")
        data = data.sort_values('Date')

        trend = data.groupby('Date')['Solde'].last().reset_index()

        plt.figure(figsize=(8, 4))
        plt.plot(trend['Date'], trend['Solde'], linewidth=2)
        plt.fill_between(trend['Date'], trend['Solde'], alpha=0.2)
        plt.title("Évolution du solde cumulé")
        plt.xlabel("Date")
        plt.ylabel("Solde (CHF)")
        plt.grid(True)

        plt.xticks(rotation=45, ha='right')
        plt.gcf().autofmt_xdate()

        plt.savefig(graphPath)


        return displayPath
