import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt


acoes = pd.DataFrame(yf.download(['LREN3.SA', 'EQTL3.SA'])['Adj Close'])

retornos_mensais = (acoes.resample('M')).last().pct_change().dropna()

fig, ax = plt.subplots()

sns.boxplot(data=retornos_mensais, orient='v')
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals = 0))

plt.show()
