import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import mplcyberpunk
import pandas as pd

cotacoes = pd.DataFrame(yf.download(["PETR4.SA"])['Adj Close'])

retornos_diarios = cotacoes.resample("M").last().pct_change().dropna()

fig, ax = plt.subplots()

ax.hist(retornos_diarios.values, bins = 35)
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1, decimals = 0))

plt.show()