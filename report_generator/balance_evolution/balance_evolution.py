from report_generator.generator import Generator
import pandas as pd

class BalanceEvolution(Generator):

    name="balanceEvolution"

    def generate(self, dataFrame: pd.DataFrame):

        df = dataFrame.copy()

        now = df['Date'].max()
        one_month_ago = now - pd.DateOffset(months=1)
        three_months_ago = now - pd.DateOffset(months=3)
        six_months_ago = now - pd.DateOffset(months=6)
        one_year_ago = now - pd.DateOffset(years=1)

        current_balance = df[df['Date'] == now]['Solde'].iloc[0]
        balance_1m = df[df['Date'] <= one_month_ago]['Solde'].iloc[0]
        balance_3m = df[df['Date'] <= three_months_ago]['Solde'].iloc[0]
        balance_6m = df[df['Date'] <= six_months_ago]['Solde'].iloc[0]
        # balance_1y = df[df['Date'] <= one_year_ago]['Solde'].iloc[0]


        delta_1m_value = current_balance - balance_1m
        delta_1m_percent = (delta_1m_value / balance_1m) * 100
        delta_1m_trend = '↑'if delta_1m_value > 0 else '↓'

        delta_3m_value = current_balance - balance_3m
        delta_3m_percent = (delta_3m_value / balance_3m) * 100
        delta_3m_trend = '↑'if delta_3m_value > 0 else '↓'

        delta_6m_value = current_balance - balance_6m
        delta_6m_percent = (delta_6m_value / balance_6m) * 100
        delta_6m_trend = '↑'if delta_6m_value > 0 else '↓'


        self.replace = {
            'date': str(now.strftime('%d-%m-%Y')),
            'delta_1m_value' : str(abs(round(delta_1m_value, 2))),
            'delta_1m_percent': str(abs(round(delta_1m_percent, 2))),
            'delta_1m_trend': delta_1m_trend,
            'delta_3m_value' : str(abs(round(delta_3m_value, 2))),
            'delta_3m_percent': str(abs(round(delta_3m_percent, 2))),
            'delta_3m_trend': delta_3m_trend,
            'delta_6m_value' : str(abs(round(delta_6m_value, 2))),
            'delta_6m_percent': str(abs(round(delta_6m_percent, 2))),
            'delta_6m_trend': delta_6m_trend,
            }

        self.replaceStub()

        return self.stub
