import pandas as pd
import os

diretorio_atual = os.getcwd()

os.chdir(f'{diretorio_atual}/galaxia4-pandas/dados/')

dre_cvm = pd.read_csv("dfp_cia_aberta_DRE_con_2021.csv",  
                                decimal = ",",
                                sep=';',
                                encoding = 'ISO-8859-1',
                                index_col='DT_REFER',
                                usecols = ['DT_REFER', 'DENOM_CIA', 'ESCALA_MOEDA',
                                'ORDEM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA'])

print(dre_cvm)