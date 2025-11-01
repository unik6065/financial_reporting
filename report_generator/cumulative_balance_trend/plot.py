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

        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(trend['Date'], trend['Solde'], linewidth=2)
        ax.fill_between(trend['Date'], trend['Solde'], alpha=0.2)
        ax.set_title("Évolution du solde cumulé")
        ax.set_xlabel("Date")
        ax.set_ylabel("Solde (CHF)")
        ax.grid(True)

        fig.autofmt_xdate()
        fig.tight_layout()

        fig.savefig(graphPath, bbox_inches="tight")
        plt.close(fig)


        return displayPath
