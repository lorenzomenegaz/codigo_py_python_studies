import pandas as pd
import yfinance as yf
import numpy as np
import warnings

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

indices = ['^BVSP', '^GSPC']

dados_indices = yf.download(indices, '2000-01-01')['Adj Close']

# Replace fillna(method='ffill') with ffill()
dados_indices.ffill(inplace=True)

dados_indices = dados_indices.pct_change()

retorno_ibov = dados_indices['^BVSP']
retorno_sp500 = dados_indices['^GSPC']

corr_movel = retorno_ibov.rolling(252).corr(retorno_sp500)

corr_movel.plot()
