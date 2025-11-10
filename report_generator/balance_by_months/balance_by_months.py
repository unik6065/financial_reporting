from report_generator.generator import Generator
from .bar import BalanceByMonthsBar
import pandas as pd

class BalanceByMonths(Generator):

    name="balanceByMonths"

    def generate(self, dataFrame: pd.DataFrame):

        months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    
        nbMonths = len(dataFrame.groupby(dataFrame.Date.dt.month))
        spendings = dataFrame[dataFrame['Montant'] < 0]
        earnings = dataFrame[dataFrame['Montant'] > 0]
        spendSorted = spendings.groupby(spendings.Date.dt.month)['Montant'].sum().sort_values()
        earningsSorted = earnings.groupby(earnings.Date.dt.month)['Montant'].sum().sort_values()

        plot = BalanceByMonthsBar()

        plotUrl = plot.printGraph(dataFrame)

        self.replace = {
            'nb_months' : str(nbMonths),
            'worst_month' : months[spendSorted.head(1).keys()[0] - 1],
            'worst_month_spent': str(abs(spendSorted.head(1).item())),
            'best_month': months[earningsSorted.tail(1).keys()[0] - 1],
            'best_month_earned': str(earningsSorted.tail(1).item()),
            'avg_earning': str(earningsSorted.sum() // nbMonths),
            'avg_spending': str(abs(spendSorted.sum() // nbMonths)),
            'graph_url': plotUrl
            }

        self.replaceStub()

        return self.stub
