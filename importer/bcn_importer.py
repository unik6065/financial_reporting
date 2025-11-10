import pandas as pd

from importer.categorizer import categorize_transaction
from .base_importer import BaseImporter

class BCNImporter(BaseImporter):
    def load_raw(self) -> pd.DataFrame:
        return pd.read_csv(
            self.file_path,
            sep=';',
            header=11,
            encoding='latin1',
            on_bad_lines='skip'
        )
    
    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        df = super().preprocess(df)
        df['Category'] = df['Libellé'].apply(categorize_transaction)
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        return df
