# Animação do desempenho do preço do dólar desde 2008

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
import mplcyberpunk


dolar = yf.download(["USDBRL=X"], "2007-12-28", "2023-01-01")['Adj Close']

dolar = dolar.resample("M").last()

plt.style.use("cyberpunk")

fig, ax = plt.subplots()
ax.set_xlim(date(2008, 1, 1), date(2022, 12, 31))
ax.set_ylim(0.5, 6)
ax.yaxis.set_major_formatter('R${x:1.0f}')
ax.set_title("Dólar x Real")

def animate(i):
    
    data = dolar.iloc[:int(i+1)] #select data range
    ax.plot(data.index, data.values, color = "#00FFFF")
    
    
ani = FuncAnimation(fig, animate, frames = range(0, len(dolar)), interval=50, repeat = False)

plt.show()