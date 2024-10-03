cotacoes = []

for c in range(1, 6):
    cotacao = float(input(f'Digite a cotação da empresa {c}: '))
    cotacoes.append(cotacao)

print(f'\nA maior cotação lida foi R${max(cotacoes)} e a menor R${min(cotacoes)}')