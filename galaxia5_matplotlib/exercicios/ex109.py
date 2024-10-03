#Crie uma animação com a correlação móvel do ibovespa x WEGE3 e VALE3 entre 2010 e 2014.
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import matplotlib.ticker as mtick
import numpy as np
from datetime import date
import matplotlib.dates as mdate
import yfinance as yf   
from datetime import datetime
import os
import mplcyberpunk

dolar = yf.download(["USDBRL=X"], "2007-12-28", "2023-01-01")['Adj Close']

dolar = dolar.resample("M").last()

acoes = ["WEGE3.SA", "VALE3.SA", "^BVSP"]

cotacoes = yf.download(acoes, "2009-01-01", "2015-01-01")['Adj Close']

retornos = cotacoes.pct_change().dropna()

acoes.remove("^BVSP")

janela_cor_weg = retornos['WEGE3.SA'].rolling(252).corr(retornos["^BVSP"]).dropna()
janela_cor_vale = retornos['VALE3.SA'].rolling(252).corr(retornos["^BVSP"]).dropna()

janela_cor_weg = janela_cor_weg.resample("M").mean()
janela_cor_vale = janela_cor_vale.resample("M").mean()

plt.style.use("cyberpunk")

fig, ax = plt.subplots()
ax.set_xlim(date(2010, 1, 1), date(2015, 1, 1))
ax.set_ylim(0, 1)
ax.set_title("Janela de correlação 12M x Ibovespa", fontweight ="bold")


def animate(i):
    
    data = janela_cor_weg.iloc[:int(i+1)] 
    weg = ax.plot(data.index, data.values, color = "#00FFFF", label = "WEGE3")
    data = janela_cor_vale.iloc[:int(i+1)] 
    vale = ax.plot(data.index, data.values, color = "fuchsia", label = "VALE3")
    
    if i == 0:
        ax.legend(["WEGE3", "VALE3"])


ani = FuncAnimation(fig, animate, frames = range(0, len(dolar)), interval=30, repeat = False)

plt.show()
