import pandas as pd
import pandas_ta as ta

df = pd.read_csv('https://raw.githubusercontent.com/nextynewb/um-python-bootcamp/main/dataset/BTC_1h.csv')
df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]


df['EMA_26'] = ta.ema(df['close'], length=26)
df['EMA_50'] = ta.ema(df['close'], length=50)

balance = 10000
btc_holdings = 0
trades = []
position = 'CASH'


for idx, row in df.iterrows():
    if idx < 26:
        continue

    prev_data = df.loc[idx-1]
    current_data = df.loc[idx]

    """
    If previous EMA_26 is less than or equal to previous EMA_50 AND current EMA_26 is greater than current EMA_50 AND position is CASH, then buy.
    If previous EMA_26 is greater than or equal to previous EMA_50 AND current EMA_26 is less than current EMA_50 AND position is IN_POSITION, then sell.

    If buy: -

    btc_holdings = balance / current_data['close']
    Then update the position to IN_POSITION

    If sell: -

    balance = btc_holdings * current_data['close']
    Then update the position to CASH
    
    """


