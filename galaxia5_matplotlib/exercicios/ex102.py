import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import mplcyberpunk
from datetime import datetime, timedelta


plt.style.use('cyberpunk')

cotacoes = yf.download(["^BVSP", "ABEV3.SA"], "2010-01-01")['Adj Close']

retorno_1_ano = (cotacoes.pct_change(periods = 252).dropna()).iloc[-1, :]
retorno_3_anos = (cotacoes.pct_change(periods = 252 * 3).dropna()).iloc[-1, :]
retorno_5_anos = (cotacoes.pct_change(periods = 252 * 5).dropna()).iloc[-1, :]
retorno_10_anos = (cotacoes.pct_change(periods = 252 * 10).dropna()).iloc[-1, :]

valores_ibov = np.array([retorno_1_ano.iloc[0], retorno_3_anos.iloc[0], retorno_5_anos.iloc[0], retorno_10_anos.iloc[0]]) * 100
valores_abev = np.array([retorno_1_ano.iloc[1], retorno_3_anos.iloc[1], retorno_5_anos.iloc[1], retorno_10_anos.iloc[1]]) * 100

fig, ax = plt.subplots(figsize = (9, 5))

numero_de_anos = 4
posicao_barras = np.arange(numero_de_anos)
largura_barras = 0.3

barras = ax.bar(posicao_barras, valores_ibov , label = "Ibovespa", width=largura_barras)
barras2 = ax.bar(posicao_barras + largura_barras, valores_abev, label = "Ambev", width=largura_barras)
plt.xticks(posicao_barras + largura_barras / 2, ("1 ano", "3 anos", "5 anos", "10 anos"))
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

#adicionando legenda de números

ax.bar_label(barras, fmt = "%.0f%%")
ax.bar_label(barras2, fmt = "%.0f%%")

plt.legend()
plt.title("Performance acumulada IBOVESPA x ABEV3")

plt.show()