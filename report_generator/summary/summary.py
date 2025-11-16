from report_generator.generator import Generator
import pandas as pd

class Summary(Generator):

    name="summary"

    def generate(self, dataFrame: pd.DataFrame):

        debits = dataFrame[dataFrame['Montant'] < 0]
        credits = dataFrame[dataFrame['Montant'] > 0]

        totalDeb = round(debits['Montant'].sum(), 2)
        totalCred = round(credits['Montant'].sum(), 2)
        diff = round(totalCred + totalDeb, 2)

        final_balance = dataFrame.head(1)['Solde'].item()
        initial_balance = dataFrame.tail(1)['Solde'].item()

        nb_transactions = dataFrame['Date'].count()
        nb_transactins_earning = credits['Montant'].count()
        nb_transactions_spending = debits['Montant'].count()

        self.replace = {
            'spent_amount' : str(abs(totalDeb)),
            'earnt_amount' : str(totalCred),
            'delta_sign': "Positif" if diff > 0 else "Négatif",
            'delta_value' : str(diff),
            'final_balance': str(final_balance),
            'balance_percent': str(round((final_balance - initial_balance) / initial_balance * 100, 2)),
            'transaction_count': str(nb_transactions),
            'earning_count': str(nb_transactins_earning),
            'spending_count': str(nb_transactions_spending),
            'avg_earning': str(round(totalCred / nb_transactins_earning, 2)),
            'avg_spending': str(abs(round(totalDeb / nb_transactions_spending, 2))),
            'ratio_earning_spending' : str(round(totalCred / abs(totalDeb) * 100, 2))
            }

        self.replaceStub()

        return self.stub
