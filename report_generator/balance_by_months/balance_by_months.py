from report_generator.generator import Generator
from .bar import BalanceByMonthsBar
import pandas as pd
import calendar

class BalanceByMonths(Generator):

    name="balanceByMonths"

    def generate(self, dataFrame: pd.DataFrame):

        months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    
        nbMonths = len(dataFrame.groupby(dataFrame.Date.dt.month))
        spendings = dataFrame[dataFrame['Montant'] < 0]
        earnings = dataFrame[dataFrame['Montant'] > 0]
        nbMonthsEarnings = len(earnings.groupby(earnings.Date.dt.month))
        nbMonthsSpendings = len(spendings.groupby(spendings.Date.dt.month))
        spendSorted = spendings.groupby(spendings.Date.dt.month)['Montant'].sum().sort_values()
        earningsSorted = earnings.groupby(earnings.Date.dt.month)['Montant'].sum().sort_values()

        plot = BalanceByMonthsBar()

        plotUrl = plot.printGraph(dataFrame)

        self.replace = {
            'table' : self.generateTable(spendings),
            'nb_months' : str(nbMonths),
            'worst_month' : months[spendSorted.head(1).keys()[0] - 1],
            'worst_month_spent': str(abs(spendSorted.head(1).item())),
            'best_month': months[earningsSorted.tail(1).keys()[0] - 1],
            'best_month_earned': str(earningsSorted.tail(1).item()),
            'avg_earning': str(earningsSorted.sum() // nbMonthsEarnings),
            'avg_spending': str(abs(spendSorted.sum() // nbMonthsSpendings)),
            'graph_url': plotUrl
            }

        self.replaceStub()

        return self.stub
    
    def generateTable(self, dataFrame: pd.DataFrame) -> str: 

        trendSpending = dataFrame.groupby(dataFrame.Date.dt.month)['Montant'].sum()


        markdown_lines = ["| Mois | Montant |", "|:-----------|-----------:|"]


        for month, amount in trendSpending.items():
            month_name = calendar.month_name[int(month)] 
            markdown_lines.append(f"| {month_name} | {amount:.2f} |")

        return "\n".join(markdown_lines)
