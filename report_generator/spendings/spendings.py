from report_generator.generator import Generator
import pandas as pd

class Spendings(Generator):

    name="spendings"

    def generate(self, dataFrame: pd.DataFrame):

        debits = dataFrame[dataFrame['Montant'] < 0]

        first_day  = pd.Timestamp(dataFrame.head(1)['Date'].item())
        last_day =  pd.Timestamp(dataFrame.tail(1)['Date'].item())

        nbMonth = pd.Timedelta(first_day - last_day).days // 30

        totatlDeb = debits['Montant'].sum()

        self.replace = {
            'spent_amount' : str(abs(round(totatlDeb, 2))),
            'spent_mean_per_month': str(abs(round(totatlDeb // nbMonth, 2)))
            }

        self.replaceStub()

        return self.stub
