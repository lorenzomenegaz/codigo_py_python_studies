import yfinance as yf
import pandas as pd
from datetime import datetime 

ticker = str(input('Ticker: ')).upper() + '.SA'
data_inicial = str(input('Data inicial: '))

data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()

acao = yf.download(ticker, data_inicial, '2022-06-30')

acao = pd.DataFrame(acao)

acao['mes'] = acao.index.month
acao['ano'] = acao.index.year

acao['volume_financeiro'] = acao['Volume'] * acao['Close']

volume_medio_mensal = acao.groupby(['ano', 'mes'])['volume_financeiro'].mean()

volume_medio_mensal = volume_medio_mensal.astype(int)

print(f'O volume médio em mês para mês de {ticker}, foi de \n{volume_medio_mensal}')
