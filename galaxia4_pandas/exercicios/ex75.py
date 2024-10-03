import pandas as pd
import yfinance as yf

acoes = yf.download(['TRPL4.SA', 'SIMH3.SA', 'CEAB3.SA', 'ABCB4.SA', 'BBDC4.SA'])['Adj Close']

acoes = acoes.reset_index().dropna()

acoes_melt = pd.melt(frame=acoes, id_vars='Date', var_name='empresa', value_name='cotacao')

acoes_pivot = pd.pivot_table(data=acoes_melt, index='Date', columns='empresa', values='cotacao')

print(acoes_pivot)