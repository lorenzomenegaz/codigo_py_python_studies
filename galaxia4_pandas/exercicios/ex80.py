import pandas as pd
import yfinance as yf
from datetime import datetime

dados_empresa_ibov = yf.download(['VALE3.SA', '^BVSP'], start='2018-01-01', end=datetime.now())['Adj Close']

dias_uteis_1y = 252

dados_12m = dados_empresa_ibov.pct_change(periods=dias_uteis_1y).dropna()

dados_12m.plot()