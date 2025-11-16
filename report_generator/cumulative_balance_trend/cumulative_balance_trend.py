from report_generator.generator import Generator
from .plot import CumulativeBalanceTrend
import pandas as pd

class Heading(Generator):

    name="cumulativeBalanceTrend"

    def generate(self, dataFrame: pd.DataFrame):

        first_transaction  = dataFrame.tail(1)
        last_transaction =  dataFrame.head(1)
        trend_direction =  'positive' if last_transaction['Solde'].item() > first_transaction['Solde'].item() else 'négative' 

        plot = CumulativeBalanceTrend()

        plotUrl = plot.printGraph(dataFrame)

        self.replace = {
            'starting_balance' : str(first_transaction['Solde'].item()),
            'ending_balance' : str(last_transaction['Solde'].item()),
            'trend_direction': trend_direction,
            'balance_delta': str(last_transaction['Solde'].item() - first_transaction['Solde'].item()),
            'balance_percent': str(round(((last_transaction['Solde'].item() - first_transaction['Solde'].item())/ first_transaction['Solde'].item())* 100, 2)),
            'graph_url': plotUrl
            }

        self.replaceStub()

        return self.stub
