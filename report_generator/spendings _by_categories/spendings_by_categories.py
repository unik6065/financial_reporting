from report_generator.generator import Generator
from .pie import SpendingByCategoriesPie
import pandas as pd

class SpendingsByCategories(Generator):

    name="spendingsByCategories"

    def generate(self, dataFrame: pd.DataFrame):

        debits = dataFrame[dataFrame['Montant'] < 0]

        debits = debits.groupby(['Category']).Montant.sum()

        plot = SpendingByCategoriesPie()

        plotUrl = plot.printGraph(debits)

        self.replace = {
            'table' : self.generateTable(debits),
            'food_percent': str(round(abs(debits['Courses alimentaires']) / abs(debits.sum()) * 100, 2)),
            'subscriptions_percent': str(round(abs(debits['Abonnements']) / abs(debits.sum()) * 100, 2)),
            'bills_percent': str(round(abs(debits['Factures / virements']) / abs(debits.sum()) * 100, 2)),
            'other_percent': str(round(abs(debits['Autres']) / abs(debits.sum()) * 100, 2)),
           'graph_placeholder': plotUrl
        }

        self.replaceStub()

        return self.stub
    
    def generateTable(self, dataFrame: pd.DataFrame) -> str: 

        if isinstance(dataFrame, pd.Series):
            df = dataFrame.reset_index()
            df.columns = ['Catégorie', 'Montant']
        else:
            df = dataFrame.copy()

        df = df.sort_values('Montant')        
            
        df['Montant'] = df['Montant'].apply(lambda x: f"{x:,.2f} CHF".replace(",", " ").replace("-", ""))

        markdown_lines = ["| Catégorie | Montant |", "|:-----------|-----------:|"]
        for _, row in df.iterrows():
            markdown_lines.append(f"| {row['Catégorie']} | {row['Montant']} |")

        return "\n".join(markdown_lines)
        