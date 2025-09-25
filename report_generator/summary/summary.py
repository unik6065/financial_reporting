from report_generator.generator import Generator
import pandas as pd

class Summary(Generator):

    name="summary"

    def generate(self, dataFrame: pd.DataFrame):

        debits = dataFrame[dataFrame['Montant'] < 0]
        credits = dataFrame[dataFrame['Montant'] > 0]

        totalDeb = debits['Montant'].sum()
        totalCred = credits['Montant'].sum()
        diff = totalCred - totalDeb

        self.replace = {
            'spent_amount' : str(abs(totalDeb)),
            'earnt_amount' : str(totalCred),
            'delta_sign': "Positif" if diff > 0 else "Négatif",
            'delta_value' : str(diff)
            }

        self.replaceStub()

        return self.stub
