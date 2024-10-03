import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdate


acao = yf.download('PETR4.SA')['Close'].dropna()

fig, ax = plt.subplots()

ax.plot(acao.index, acao.values)

ax.yaxis.set_major_formatter('R${x:1.0f}')

ax.xaxis.set_major_locator(mdate.YearLocator(2))

formatacao = mdate.DateFormatter('%d-%b-%Y')

ax.xaxis.set_major_formatter(formatacao)

plt.xticks(rotation=45)

plt.show()