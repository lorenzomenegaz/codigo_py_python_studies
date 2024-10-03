import numpy as np

retornos = int(input('Digite quantos retornos devem ser gerados: '))

retornos_gerados = np.random.uniform(-1, 1, retornos)

retornos_positivos_gerados = retornos_gerados[retornos_gerados > 0]

print(f'Os retornos positivos gerados foram: {retornos_positivos_gerados}')
print(f'O primeiro retorno foi {retornos_gerados[0]} e o último foi {retornos_gerados[-1]}')