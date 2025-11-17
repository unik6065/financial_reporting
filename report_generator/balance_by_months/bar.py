import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class BalanceByMonthsBar():

    def printGraph(self, dataFrame: pd.DataFrame):

        graphPath = './hello/graphs/BalanceByMonths.png'
        displayPath = './graphs/BalanceByMonths.png'

        data = dataFrame.copy()
        data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, format="mixed")
        data = data.sort_values('Date')

        spendings = data[data['Montant'] < 0]
        nbMonthsSpendings = len(spendings.groupby(spendings.Date.dt.month))
        earnings = data[data['Montant'] > 0]
        nbMonthsEarnings = len(earnings.groupby(earnings.Date.dt.month))


        trendSpending = spendings.groupby(spendings.Date.dt.month)['Montant'].sum()
        trendEarning = earnings.groupby(earnings.Date.dt.month)['Montant'].sum()

        months = np.arange(1, 13)
        trendSpending = trendSpending.reindex(months, fill_value=0)
        trendEarning = trendEarning.reindex(months, fill_value=0)

        spendAvg = abs(trendSpending.sum())/nbMonthsSpendings 
        earnAvg = trendEarning.sum()/nbMonthsEarnings 
        
        fig, ax = plt.subplots(figsize=(10, 5))

        width = 0.4

        ax.bar(months - width/2, trendEarning, width=width, color='green', label='Revenus')
        ax.bar(months + width/2, abs(trendSpending), width=width, color='red', label='Dépenses')

        ax.axhline(y=earnAvg, color='green', linestyle='--', label='Revenu Moyen')
        ax.axhline(y=spendAvg, color='red', linestyle='--', label='Dépenses Moyenne')

        ax.set_title("Revenus et dépenses par mois")
        ax.set_xlabel("Mois")
        ax.set_ylabel("Montant (CHF)")
        ax.set_xticks(months)
        ax.set_xticklabels([
            "Jan", "Fév", "Mar", "Avr", "Mai", "Juin", 
            "Juil", "Août", "Sep", "Oct", "Nov", "Déc"
        ])

        ax.grid(True, axis="y", linestyle="--", alpha=0.6)

        fig.tight_layout()

        fig.savefig(graphPath, bbox_inches="tight")
        plt.close(fig)


        return displayPath
