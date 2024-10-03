import pandas as pd
import os

diretorio_atual = os.getcwd()

os.chdir(f'{diretorio_atual}/galaxia4-pandas/dados/')

dados_euca3 = pd.read_excel("dados_euca3.xlsx",
                                index_col='Data',
                                na_values='nd',
                                decimal = ",",)

dados_euca3 = dados_euca3.fillna(method = 'ffill', limit = 2)

print(dados_euca3)