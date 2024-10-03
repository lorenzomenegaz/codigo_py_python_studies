import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


acao = str(input(f'Digite o ticker: ')).upper() + '.SA'

df = pd.DataFrame(yf.download(acao))['Adj Close'].dropna()

fig, ax = plt.subplots()

ax.set_xlabel('Período')
ax.set_ylabel('Cotações')
ax.set_title('Histórico de preço da ação')

ax.plot(df.index, df.values)

plt.show()