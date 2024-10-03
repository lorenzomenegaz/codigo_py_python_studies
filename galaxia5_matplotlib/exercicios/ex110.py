import quantstats as qs
import pandas as pd
import yfinance as yf


cotacao = pd.DataFrame(yf.download('wege3.SA')['Adj Close'])

retornos_mensais = cotacao.resample('M').last().pct_change().dropna()

qs.extend_pandas()

retornos_mensais.plot_monthly_heatmap()