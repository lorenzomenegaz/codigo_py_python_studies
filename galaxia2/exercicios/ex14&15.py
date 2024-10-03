simpar = {'nome': 'Simpar', 'cnpj': '07.415.333/0001-20', 'tickers': 'SIMH3', 'fundação': 1956, 'segmento': 'Holding', 'P/L': 133.03, 'ROE': '1.48%'}

print(f'''{60*'='}\n
A empresa sendo estudada é a {simpar["nome"]}
Seus indicadores de P/L são {simpar["P/L"]} e ROE {simpar['ROE']} e está empresa é do segmento de {simpar["segmento"]}\n
{60*'='}''')

print('')

escolha = input('Você compraria está empresa? ')

simpar['Compraria'] = escolha
print(simpar)