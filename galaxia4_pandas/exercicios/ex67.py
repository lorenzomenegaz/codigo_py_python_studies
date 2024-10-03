import pandas as pd

dicionario = {
       "nomes": ["Weg", "Petrobras", "Vale", "Petrobras", "Lojas Renner"],
       "tickers": ["WEGE3", "PETR3", "VALE3", "PETR4", "LREN3"],  
       "cotacoes": [20, 30, 40, 12, 35],
       "preco_sobre_lucro": [25, 6, 12, 7, 25],  
       "volume": [5000, 1000, 4000, 7000, 1200]
}

df_info_empresas = pd.DataFrame(dicionario)

df_info_empresas = df_info_empresas.set_index("tickers")

df_info_empresas.columns = ['nomes', 'precos', 'preco_sobre_lucro', 'volume']

df_info_empresas['lpa'] = df_info_empresas['precos'] / df_info_empresas['preco_sobre_lucro']

dolar = 5.25

df_info_empresas['precos_dolar'] = df_info_empresas['precos'] / dolar

print(df_info_empresas.sort_values(by = 'volume', ascending = False).drop_duplicates(subset = 'nomes'))
