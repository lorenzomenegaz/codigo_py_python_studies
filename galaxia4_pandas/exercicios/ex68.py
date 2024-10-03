import pandas as pd
import yfinance as yf

dados_mglu = pd.DataFrame(yf.download('MGLU3.SA'))

dados_mglu['Adj Close'] = dados_mglu['Adj Close'].astype(int)

print(dados_mglu)