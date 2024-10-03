lista_numerica = [2, 4, 5, 6, 10]

lista_filtrada = list(filter(lambda num: num > 5, lista_numerica))

print(f'Lista filtrada para números > 5: {lista_filtrada}')