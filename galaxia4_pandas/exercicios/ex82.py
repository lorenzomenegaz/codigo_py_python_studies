import pandas as pd
import yfinance as yf  
import numpy as np

acao = yf.download('WEGE3.SA', '2020-01-01')['Close']

acao = acao.to_frame().dropna()

acao['EWM'] = acao.ewm(span = 30).mean()

acao.plot()