import matplotlib.pyplot as plt
import yfinance as yf


cotacoes = yf.download(["^BVSP"], "1994-01-01")['Adj Close']

fig, ax = plt.subplots(2, 1, figsize = (20, 20))

ax[0].plot(cotacoes.index, cotacoes.values)

ax[1].plot(cotacoes.index, cotacoes.values)
ax[1].set_yscale('log')