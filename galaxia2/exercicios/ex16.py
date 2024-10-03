nome_empresa = input('Digite o nome de uma empresa: ')

print(f'A primeira letra é {nome_empresa[0]}')
print(f'A última letra é {nome_empresa[-1]}')
print(f'O nome da empresa contém {len(nome_empresa)} letras')
print(f'{nome_empresa.upper()}')
print(nome_empresa.capitalize())

print(f"{nome_empresa.replace(nome_empresa[0:2], 'tranqueira')}")