import numpy as np
import random

vetor_aleatorio = list(np.random.randint(low = 0, high = 60, size= 6))

vetor_valido = []

for numero in vetor_aleatorio:

    while vetor_aleatorio.count(numero) > 1:
        numero = random.randint(0, 60)

    vetor_valido.append(numero)

print(f'Este são os seis números que trouxemos para você {vetor_valido}')
print('A probabilidade de você acertar é de 1 em 50.063.860')
