import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


acoes = []

for n in range(0, 4):
    acao = str(input(f'Digite o ticker: ')).upper() + '.SA'
    acoes.append(acao)

df_acoes = pd.DataFrame(yf.download(acoes)['Adj Close']).dropna()

fig, ax = plt.subplots()

for acao in df_acoes.columns:

    ax.plot(df_acoes.index, df_acoes[acao].values, label = acao)

    ax.legend()