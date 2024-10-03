import pandas as pd
import yfinance as yf

dados_acao = yf.download(["CASH3.SA", 'LJQQ3.SA', 'PETR4.SA'], "2015-01-01", "2022-01-01")['Adj Close']

dados_acao_without_na = dados_acao.dropna()

print(dados_acao_without_na)

dados_acao = dados_acao.dropna(subset = ['LJQQ3.SA'])

print(dados_acao.drop('PETR4.SA', axis = 1))
