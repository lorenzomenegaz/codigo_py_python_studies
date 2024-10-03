import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk


plt.style.use("cyberpunk")

acoes_df = pd.DataFrame(yf.download(['SLCE3.SA', 'BBDC4.SA', 'TRPL4.SA', 'SBSP3.SA', '^BVSP'])['Close']).dropna()

retornos = acoes_df.pct_change()

retorno_ibov = retornos['^BVSP']

retornos = retornos.drop('^BVSP', axis = 1)

corr_movel = (retornos.rolling(252).corr(retorno_ibov)).dropna()

corr_movel.plot(figsize=(16, 10))
