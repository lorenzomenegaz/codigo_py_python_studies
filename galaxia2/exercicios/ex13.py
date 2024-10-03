# crie um programa que receba o nome de usuário, de boas vindas e colete informações de 2 carteiras de investimentos com 3 nomes de empresa cada.
# devolva pro usuário a interseção entre carteiras de investimentos, a diferença e a uniao entre elas

x = 0
lista_temporaria = []

while x <=2:
    lista_temporaria.append(input(f'Digite o nome de 3 empresas da sua primeira carteira:'))
    x += 1
while x <=5:
    lista_temporaria.append(input(f'Digite o nome de 3 empresas da sua segunda carteira:'))
    x += 1

set1 = {lista_temporaria[0], lista_temporaria[1],lista_temporaria[2]}
set2 = {lista_temporaria[3], lista_temporaria[4], lista_temporaria[5]}

print(f'''A interseção entre as duas carteiras ficam {set1.intersection(set2)}\n
A diferença das duas carteiras é {set1.difference(set2)}\n
A união entre as duas carteiras é {set1.union(set2)}''')
