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

dataframe.columns = ["nomes", "precos", "preco_sobre_lucro", "volume"] #pode ser feito assim tmb: df = dataframe.rename(columns={'cotacoes': 'prices'})

dataframe['LPA'] = dataframe['precos']/dataframe['preco_sobre_lucro']
dataframe['cotacoes_dolarizadas'] = dataframe['precos']/5.25

volume_total = dataframe['volume'].sum()

print(volume_total)