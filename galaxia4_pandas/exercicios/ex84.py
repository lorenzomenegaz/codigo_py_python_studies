import pandas as pd
import yfinance as yf
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

acoes = ['INBR32.SA', 'DMVF3.SA', 'ANIM3.SA', 'SIMH3.SA', 'TEND3.SA', 'MDNE3.SA', 'VAMO3.SA']
dados_acoes = yf.download(acoes, '2023-01-01', '2024-05-01')['Adj Close']

dados_acoes.ffill(inplace=True)

dados_acoes.corr()

