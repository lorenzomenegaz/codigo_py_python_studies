import numpy as np
import pandas as pd

cotacao_inicial = float(input("Qual a cotação inicial da ação? "))

periodo_projecao = 30
lista_cotacoes = [cotacao_inicial]
lista_dias = [0]
volatilidade_diaria = 0.01

for i in range(1, periodo_projecao):
    
    cotacao_seguinte = lista_cotacoes[-1] * (1 + np.random.normal(0, volatilidade_diaria))
    
    lista_cotacoes.append(cotacao_seguinte)
    lista_dias.append(i)
    
serie_final = pd.Series(lista_cotacoes, index = lista_dias)

print(serie_final)
