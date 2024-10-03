import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

um_ano_atras = datetime.now() - timedelta(days = 365)

acao = str(input(f'Digite o ticker: ')).upper() + '.SA'

df = pd.DataFrame(yf.download(acao, um_ano_atras))['Adj Close']

fig, ax = plt.subplots()

rentabilidade = df.iloc[-1]/df.iloc[0] - 1
print(rentabilidade)

if rentabilidade > 0:

    ax.plot(df.index, df.values)
    ax.set_ylabel("Cotação não dá ré", labelpad = 15, fontsize = 12)

else: 
    
    ax.plot(df.index, df.values)
    ax.set_ylabel("Cotação afundando", labelpad = 15, fontsize = 12)

ax.set_xlabel("Sou sardinha olhando curto prazo", labelpad = 15, fontsize = 12)

plt.show()
