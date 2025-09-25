from report_generator.generator import Generator
from .pie import TopMonthSpendingsPie
import pandas as pd

class TopMonthSpendings(Generator):

    name="topMonthSpendings"


    def generate(self, dataFrame: pd.DataFrame):

        debits = dataFrame[dataFrame['Montant'] < 0]
        debits = debits.sort_values('Montant').head(5)

        pie = TopMonthSpendingsPie()

        graphUrl = pie.printGraph(debits)

        self.replace = {
            'first_spending' : str(debits.iloc[0]['Libell�']),
            'first_spending_amount': str(abs(debits.iloc[0]['Montant'])),
            'second_spending' : str(debits.iloc[1]['Libell�']),
            'second_spending_amount': str(abs(debits.iloc[1]['Montant'])),
            'third_spending' : str(debits.iloc[2]['Libell�']),
            'third_spending_amount': str(abs(debits.iloc[2]['Montant'])),
            'fourth_spending' : str(debits.iloc[3]['Libell�']),
            'fourth_spending_amount': str(abs(debits.iloc[3]['Montant'])),
            'fifth_spending' : str(debits.iloc[4]['Libell�']),
            'fifth_spending_amount': str(abs(debits.iloc[4]['Montant'])),
            'chart_url': graphUrl
        }

        self.replaceStub()

        return self.stub
