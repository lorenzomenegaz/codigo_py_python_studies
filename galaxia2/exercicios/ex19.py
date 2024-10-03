nome_empresa = str(input('Digite o nome da empresa: ')).capitalize()
pl_empresa = float(input('Digite o Preço sobre Lucro(PL) da empresa: '))

roe_empresa = float(input('Digite o ROE da empresa: '))
porcentagem_roe = '{:.0%}'.format(roe_empresa)

if roe_empresa > 0.2 and pl_empresa > 20:
    print(f'A empresa {nome_empresa} está muito cara!')

elif roe_empresa >= 0.2 and pl_empresa <= 8:
    print('Pelos indicadores passados, recomendamos compra!')

else:
    print('Recomendamos estudar mais sobre a ação')