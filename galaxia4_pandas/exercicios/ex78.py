import yfinance as yf
import pandas as pd

vale = yf.download('VALE3.SA')['Adj Close']

dados_vale_30min = vale.resample('30T').last()
dados_vale_week = vale.resample('W').last()
dados_vale_month = vale.resample('M').last()
dados_vale_year = vale.resample('Y').last()

print(dados_vale_year)