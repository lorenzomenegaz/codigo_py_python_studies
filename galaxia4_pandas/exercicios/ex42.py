import pandas as pd

dicionario = {
       "nomes": ["Weg", "Petrobras", "Vale", "Petrobras", "Lojas Renner"],
       "tickers": ["WEGE3", "PETR3", "VALE3", "PETR4", "LREN3"],  
       "cotacoes": [20, 30, 40, 12, 35],
       "preco_sobre_lucro": [25, 6, 12, 7, 25],  
       "volume": [5000, 1000, 4000, 7000, 1200]
}

dataframe = pd.DataFrame(dicionario)
dataframe = dataframe.set_index('tickers')
colunas = dataframe.columns = ["nomes", "tickers", "precos", "preco_sobre_lucro", "volume"]

print(dataframe[colunas[3:]])