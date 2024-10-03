import pandas as pd
import os

diretorio_atual = os.getcwd()

os.chdir(f'{diretorio_atual}/galaxia4-pandas/dados/')

dados_petrobras = pd.read_excel("exercicio_receita_petro.xlsx",  
                                skiprows=4, 
                                index_col='Data', 
                                na_values='nd',
                                decimal = ".",
                                usecols =['Data', 'Receita Líquida 12 meses Consolidado Milhões', 'Convenção'])


print(dados_petrobras)