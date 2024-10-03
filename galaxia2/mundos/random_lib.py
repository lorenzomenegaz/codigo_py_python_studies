import random

from random import choice

valor_entre_0_ou_1 = random.random()
print(valor_entre_0_ou_1)

valor_decimal_de_igual_probabilidade_entre_valores = random.uniform(10, 100)
print(valor_decimal_de_igual_probabilidade_entre_valores)

valor_inteiro_de_igual_probabilidade_entre_valores = random.randint(10, 100)
print(valor_inteiro_de_igual_probabilidade_entre_valores)

valor_dist_normal = random.gauss(10, 30)
print(valor_dist_normal)

#sorteio, importando a função direto.

tickers = ['WEGE3', 'PCAR3', 'LREN3']

empresa_escolhida = choice(tickers)
print(empresa_escolhida)