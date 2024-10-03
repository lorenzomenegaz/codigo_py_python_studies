# criar dicionarios
dicionario_vazio = {}

dicionario_povoado = dict({'nome': 'brenno', 'sobrenome': 'sullivan'})

dicionario_numerico = dict({1: 'brenno', 2: 'lucas', 3: 'leandro'})

dicionario_com_listas = {'empresas_novo_mercado': ['Weg', 'Renner', 'Vale'],
                         'empresas_em_outro_segmento': ['Petrobras', 'Alpargatas'],}

dicionario_empresas_na_carteira = {True: ['Pão de açucar', 'Weg'],
                                   False: ['Lojas Renner', 'Gurarapes']}

# pegando itens dentro do dicionário
print(dicionario_numerico[2])
print(dicionario_numerico.get(2))
print(dicionario_povoado.get('nome'))
print(dicionario_com_listas['empresas_novo_mercado'])
print(dicionario_com_listas['empresas_novo_mercado'][0])

# adicionar elementos a um dicionario
dicionario_vazio['Curso'] = 'codigo.py'
dicionario_vazio.update({'Galáxia': 2, 'Mundo': 13})

print(dicionario_vazio)

# removendo dados de um dicionário
dicionario_vazio.pop('Curso')

print(dicionario_vazio)

# -+- aplicabilidades de um dicionário -+-

import pandas as pd

# tabela de cotações