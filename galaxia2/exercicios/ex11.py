import random
from random import choice

x = 0
acoes = []
while x <= 3:
    y = input('Digite o nome de quatro ações que iramos indicar uma dentre as digitadas: ')
    x += 1
    acoes.append(y)

acao_escolhida = choice(acoes)
print(f'A ação recomendada foi {acao_escolhida}')