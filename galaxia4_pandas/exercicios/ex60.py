import pandas as pd
import yfinance as yf
from datetime import datetime


stocks = ['WEGE3.SA', 'PCAR3.SA', 'ABEV3.SA', 'CASH3.SA', 'RADL3.SA']

dados = yf.download(tickers = stocks, 
                           start = "2018-12-31", end = datetime.now())['Adj Close']

print(dados)