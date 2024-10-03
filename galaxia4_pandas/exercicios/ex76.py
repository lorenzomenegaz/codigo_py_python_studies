import pandas as pd
import yfinance as yf

mglu = yf.download('MGLU3.SA').dropna()
bhia = yf.download('BHIA3.SA').dropna()

mglu['Ticker'] = ['MGLU3'] * len(mglu)
bhia['Ticker'] = ['BHIA3'] * len(bhia)

concat = pd.concat([mglu, bhia], ignore_index=True)

print(concat)