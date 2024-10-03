import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta


um_mes_atras = datetime.now() - timedelta(days = 30)
tres_meses_atras = datetime.now() - timedelta(days = 90)
um_ano_atras = datetime.now() - timedelta(days = 365)
tres_anos_atras = datetime.now() - timedelta(days = 1095)

timestamps = [um_mes_atras, tres_meses_atras, um_ano_atras, tres_anos_atras]
titles = ['Um mês', 'Três meses', 'Um ano', 'Três anos']

acao = str(input(f'Digite o ticker: ')).upper() + '.SA'

df = pd.DataFrame(yf.download(acao))['Adj Close'].dropna()

fig, ax = plt.subplots(2, 2, figsize = (30, 15))

coluna = 0

for periodo in timestamps:
    
    if periodo == um_mes_atras:
        
        cot_periodo = df[df.index > periodo]
        ax[0, 0].set_xlim(periodo, datetime.now())
        ax[0, 0].set_ylim(np.min(cot_periodo) - 5, np.max(cot_periodo) + 5)
        ax[0, 0].plot(cot_periodo.index, cot_periodo.values)
        ax[0, 0].set_title(titles[coluna])
        
    elif periodo == tres_meses_atras:
        
        cot_periodo = df[df.index > periodo]
        ax[0, 1].set_xlim(periodo, datetime.now())
        ax[0, 1].set_ylim(np.min(cot_periodo) - 5, np.max(cot_periodo) + 5)
        ax[0, 1].plot(cot_periodo.index, cot_periodo.values)
        ax[0, 1].set_title(titles[coluna])
    
    elif periodo == um_ano_atras:
        
        cot_periodo = df[df.index > periodo]
        ax[1, 0].set_xlim(periodo, datetime.now())
        ax[1, 0].set_ylim(np.min(cot_periodo) - 5, np.max(cot_periodo) + 5)
        ax[1, 0].plot(cot_periodo.index, cot_periodo.values)
        ax[1, 0].set_title(titles[coluna])
        
    else:
        
        cot_periodo = df[df.index > periodo]
        ax[1, 1].set_xlim(periodo, datetime.now())
        ax[1, 1].set_ylim(np.min(cot_periodo) - 5, np.max(cot_periodo) + 5)
        ax[1, 1].plot(cot_periodo.index, cot_periodo.values)
        ax[1, 1].set_title(titles[coluna])

    coluna += 1
        
plt.show()