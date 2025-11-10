from report_generator.generator import Generator
import pandas as pd

class Earnings(Generator):

    name="earnings"

    def generate(self, dataFrame: pd.DataFrame):

        credits = dataFrame[dataFrame['Montant'] > 0]

        first_day  = pd.Timestamp(dataFrame.head(1)['Date'].item())
        last_day =  pd.Timestamp(dataFrame.tail(1)['Date'].item())

        nbMonth = pd.Timedelta(first_day - last_day).days // 30

        totatlDeb = credits['Montant'].sum()

        self.replace = {
            'earnt_amount' : str(abs(round(totatlDeb, 2))),
            'earnt_mean_per_month': str(abs(round(totatlDeb // nbMonth, 2)))
            }

        self.replaceStub()

        return self.stub
