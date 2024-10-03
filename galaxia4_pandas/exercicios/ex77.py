import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta

acoes = ['CEAB3.SA', 'SIMH3.SA', 'SLCE3.SA']

dia = datetime.now() - timedelta(days = 1)

dados_cotacoes = yf.download(acoes, dia)['Close']
dados_cotacoes = pd.melt(frame=dados_cotacoes, var_name='Empresa', value_name='Price')

dados_volume = yf.download(acoes, dia)['Volume']
dados_volume = pd.melt(frame=dados_volume, var_name='Empresa', value_name='Volume')

merge = pd.merge(dados_cotacoes, dados_volume, how = "inner", 
                on = "Empresa")

print(merge)