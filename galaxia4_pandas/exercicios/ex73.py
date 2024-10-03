import pandas as pd
import os

diretorio_atual = os.getcwd()

os.chdir(f'{diretorio_atual}/galaxia4-pandas/dados/')

dados_dy = pd.read_excel('dy_yield_empresas_26set.xlsx').dropna()

dados_dy['ranking_dividendos'] = dados_dy['DY_12M'].rank(ascending = False)

divisorias = [0, (max(dados_dy['ranking_dividendos'])/4), 
              (max(dados_dy['ranking_dividendos'])/4 * 2),  
              (max(dados_dy['ranking_dividendos'])/4 * 3),
             max(dados_dy['ranking_dividendos']) + 1]

dados_dy['quartil'] = pd.cut(dados_dy['ranking_dividendos'], divisorias)

dados_dy['rank_quartil'] = dados_dy['quartil'].rank(method = "dense")

dummies_empresas = pd.get_dummies(dados_dy['quartil'])

print(dummies_empresas)