import numpy as np

lucro_weg = float(input('Digite o lucro da Weg em milhões: '))
lucro_vale = float(input('Digite o lucro da Vale em milhões: '))
lucro_petrobras = float(input('Digite o lucro da Petrobras em milhões: '))

array = np.array([lucro_weg, lucro_vale, lucro_petrobras])

array_decrescente = -np.sort(-array)

print(array_decrescente)
