from report_generator.generator import Generator
import pandas as pd

class Heading(Generator):

    name="heading"

    def generate(self, dataFrame: pd.DataFrame):

        first_transaction  = dataFrame.tail(1)
        last_transaction =  dataFrame.head(1)


        self.replace = {
            'first_day' : str(pd.Timestamp(first_transaction['Date'].item())),
            'last_day': str(pd.Timestamp(last_transaction['Date'].item())),
            'starting_balance': str(first_transaction['Solde'].item()),
            'final_balance': str(last_transaction['Solde'].item())
            }

        self.replaceStub()

        return self.stub
