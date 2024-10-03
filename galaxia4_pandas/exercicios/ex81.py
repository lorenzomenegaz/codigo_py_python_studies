import pandas as pd
import yfinance as yf  
import numpy as np

acao = yf.download('WEGE3.SA', '2020-01-01')['Close']

acao = acao.to_frame().dropna()

acao['MM1M'] = acao.rolling(30).mean()
acao['Ordem'] = np.where(acao['Close'] > acao['MM1M'], 'Compra', 'Venda')

acao.plot()
print(acao)