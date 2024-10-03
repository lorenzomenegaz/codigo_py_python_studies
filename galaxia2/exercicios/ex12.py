x = 0
acoes_pl = []

while x <= 4:
    y = input('Digite o P/L de cinco ações da sua carteira: ')
    acoes_pl.append(float(y))
    x += 1

acoes_pl_ordenadas = sorted(acoes_pl)

print(f'Os menores P/L foram {acoes_pl_ordenadas[0]} e {acoes_pl_ordenadas[1]}')