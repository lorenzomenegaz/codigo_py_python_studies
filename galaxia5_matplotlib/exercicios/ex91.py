import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

acoes = []

for n in range(1, 4):
    acao = str(input(f'Digite o ticker: ')).upper() + '.SA'
    acoes.append(acao)

acoes.append('^BVSP')

df_acoes = pd.DataFrame(yf.download(acoes)['Adj Close']).dropna()

fig, ax = plt.subplots(2, 2, figsize = (10, 6))

coluna = 0

for i in range(2):
    for j in range(2):
        
        ax[i, j].plot(df_acoes.index, df_acoes.iloc[:, coluna])
        ax[i, j].set_title(df_acoes.columns[coluna])

        coluna = coluna + 1