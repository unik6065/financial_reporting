import pandas as pd

class BaseImporter:
    
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_raw(self) -> pd.DataFrame:
        raise NotImplementedError('Subclasses must implement load_raw()')
    
    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, format="mixed")
        df = df.dropna(subset=['Date'])
        df = df.sort_values('Date')
        return df

    
    def load(self)-> pd.DataFrame:
        df = self.load_raw()
        df = self.preprocess(df)
        return df