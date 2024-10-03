import pandas as pd
import yfinance as yf  
import numpy as np

acao = yf.download('CEAB3.SA')['Close'].dropna().to_frame()

volatilidade_diaria_12m = acao['Close'].pct_change().rolling(252).std().dropna()

volatilidade_diaria_12m = volatilidade_diaria_12m * np.sqrt(252)

volatilidade_diaria_12m.plot()
print(volatilidade_diaria_12m)