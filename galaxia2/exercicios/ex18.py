codigo_stock = str(input('Digite o código de negociação de uma ação: ')).lower()

if codigo_stock.endswith('3'):  
    print('Esse código de negociação é uma ação ON')

elif codigo_stock.endswith('4'):
    print('Esse código de negociação é uma ação PN')

elif codigo_stock.endswith('11'):
    print('Esse código de negociação é uma ação UNIT')

else:
    print('Código de negociação inválido!')