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

empresa_escolhida = input('''Qual empresa você quer saber o quartil que ela ocupa na distribuição
                          de dividendos da bolsa? ''').upper()

quartil = (dados_dy[dados_dy['TICKER'] == empresa_escolhida]).iloc[0, 5]

print(f'''A empresa {empresa_escolhida} fica localizada 
                no {quartil}º quartil em distribuição de dividendos
                de todas as empresas da bolsa.''')