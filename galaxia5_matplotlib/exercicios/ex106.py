import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

cotacoes = pd.DataFrame(yf.download(['PETR3.SA', 'PETR4.SA'])['Adj Close'])

retornos_diarios = cotacoes.pct_change().dropna()

fig, ax = plt.subplots()

sns.regplot(x = retornos_diarios['PETR3.SA'], y = retornos_diarios['PETR4.SA'], line_kws={"color" : "red" })
ax.xaxis.set_major_formatter(mtick.PercentFormatter(1, decimals = 0))
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals = 0))

plt.show()