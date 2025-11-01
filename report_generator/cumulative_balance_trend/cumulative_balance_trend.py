from report_generator.generator import Generator
from .plot import CumulativeBalanceTrend
import pandas as pd

class Heading(Generator):

    name="cumulativeBalanceTrend"

    def generate(self, dataFrame: pd.DataFrame):

        # first_transaction  = dataFrame.tail(1)
        # last_transaction =  dataFrame.head(1)


        plot = CumulativeBalanceTrend()

        dataFrame = dataFrame[['Solde', 'Date']].groupby('Date').last().reset_index()

        plotUrl = plot.printGraph(dataFrame)

        # self.replace = {
        #     'first_day' : str(pd.Timestamp(first_transaction['Date'].item())),
        #     'last_day': str(pd.Timestamp(last_transaction['Date'].item())),
        #     'starting_balance': str(first_transaction['Solde'].item()),
        #     'final_balance': str(last_transaction['Solde'].item())
        #     }

        # self.replaceStub()

        return self.stub
