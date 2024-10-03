import yfinance as yf
import mplcyberpunk
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pylab as lab
import numpy as np
import matplotlib.ticker as mtick

cotacoes = pd.DataFrame(yf.download(["^GSPC", "^BVSP"])['Adj Close'])

retornos_anuais = cotacoes.resample("Y").last().pct_change().dropna()

retornos_anuais['Ano'] = retornos_anuais.index.year

def barra_discreta(vetor_categoria):
    
    cmap = lab.cm.cool  # define a cor
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmap = mpl.colors.LinearSegmentedColormap.from_list(
        'cmap escolhido', cmaplist, cmap.N)
    bounds = np.linspace(np.min(vetor_categoria), np.max(vetor_categoria) + 0.5, len(vetor_categoria) + 1)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
    return bounds, norm

#Dispersão 

fig, ax = plt.subplots()

ax.scatter(retornos_anuais['^GSPC'], retornos_anuais["^BVSP"], c = retornos_anuais['Ano'], cmap="cool")

bounds, norm = barra_discreta(retornos_anuais['Ano'])     

#cria um novo eixo pra barra

ax2 = fig.add_axes([0.95, 0.1, 0.03, 0.8])
cb = mpl.colorbar.ColorbarBase(ax2, cmap="cool", norm=norm,
    spacing='proportional', ticks=bounds + 0.5, boundaries=bounds, format='%1i')

ax.xaxis.set_major_formatter(mtick.PercentFormatter(1, decimals = 0))
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1, decimals = 0))
ax.set_ylabel("Ibovespa")
ax.set_xlabel("SP500")
ax.axhline(y = 0)
ax.axvline(x = 0)
ax.set_title("Retornos anuais SP500 X Ibovespa")

plt.show()