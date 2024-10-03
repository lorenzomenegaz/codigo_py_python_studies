import pandas as pd
import yfinance as yf
from datetime import datetime

ibov = '^BVSP'

dados = yf.download(tickers= ibov, start = "1994-6-1", end = datetime.now())['Adj Close']

print(dados)