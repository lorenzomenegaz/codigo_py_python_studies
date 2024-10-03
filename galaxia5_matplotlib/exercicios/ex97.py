import yfinance as yf
import matplotlib.pyplot as plt


acao = yf.download('PETR4.SA')['Close'].dropna()

fig, ax = plt.subplots()

ax.plot(acao.index, acao.values)
ax.yaxis.set_major_formatter('R${x:1.0f}')

plt.show()