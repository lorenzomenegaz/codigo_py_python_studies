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
condicoes = dataframe[(dataframe['cotacoes'] > 20) | (dataframe['volume'] > 4000)]

print(condicoes)