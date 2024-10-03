# Crie um programa que receba um input de número e retorne as seguintes características do número para o usuário:
# dobro, raiz quadrada, elevado ao quadrado, dividido por dois, seu antecessor e seu sucessor.

num = float(input(f'\nDigite um número:'))

dobro = num*2
raiz = num**(1/2)
elevado = num**2
antecessor = num-1
sucessor = num+1

print(f'''\nO dobro do número é {dobro}\n
A raiz é {raiz}\n
Elevado ao quadrado é {elevado}\n
O antecessor é {antecessor} e o sucessor é {sucessor}''')