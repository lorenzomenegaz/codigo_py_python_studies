import pandas as pd
import yfinance as yf

slc = yf.download('WEGE3.SA')['Adj Close']

retorno_diario = slc.pct_change().dropna()

retorno_anual = slc.resample('Y').last()

print(retorno_diario)
print(retorno_anual)