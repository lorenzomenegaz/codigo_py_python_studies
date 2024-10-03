import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mtick
import matplotlib.dates as mdate
import yfinance as yf
from datetime import datetime


cotacoes = yf.download(["^BVSP"], "2020-01-01", "2023-01-01")['Adj Close']

data_crises = [(datetime(2020, 3, 20), "Fundo Covid"),
              (datetime(2022, 2, 24), "Guerra Russia vs Ucrânia")]

fig, ax = plt.subplots()

ax.plot(cotacoes)

for data, evento in data_crises:
    
    ax.annotate(evento, xy = (data, cotacoes.asof(data) + 5000), #posição comeco da seta
                xytext = (data, cotacoes.asof(data) + 15000), #posição texto da seta
                arrowprops = dict(facecolor = 'black', headwidth = 4, width = 2, headlength = 4),
               horizontalalignment = "left", verticalalignment = "top")


ax.xaxis.set_major_locator(mdate.YearLocator(1))
