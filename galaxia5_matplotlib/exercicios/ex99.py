import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import yfinance as yf

cotacoes = yf.download("PETR4.SA")['Close']

retornos = cotacoes.pct_change().dropna()

retornos_acumulados = (1 + retornos).cumprod() - 1

fig, ax = plt.subplots()

ax.plot(retornos_acumulados.index, retornos_acumulados.values)

ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))