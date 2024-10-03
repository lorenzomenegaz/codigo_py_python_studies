nome_empresas, roe_empresas, pl_empresas = [], [], []
contador, roe_medio, menor_pl = 0, 0, 0
print('Vamos montar sua carteira de ações')

while True:
    nome = str(input(f'Digite o nome da empresa {contador}: ')).capitalize()
    roe = float(input(f'Digite o ROE da empresa {nome}: ' ))
    pl = int(input(f'Digite o PL da empresa {nome}: '))
    nome_empresas.append(nome)
    roe_empresas.append(roe)
    pl_empresas.append(pl)

    empresa_menor_pl = nome
    roe_medio += roe

    if contador == 0:
        menor_pl = pl
        empresa_menor_pl = nome
    elif pl < menor_pl:
        menor_pl = pl
        empresa_menor_pl = nome
    else:
        pass

    contador += 1

    continuar = str(input('Deseja adicionar mais uma? (Responda com S ou N): ')).lower()

    if continuar == 'n':
        break

roe_medio = roe_medio/len(nome_empresas)
roe_medio = "{:.0%}".format(roe_medio)

print(f'A carteira tem {len(nome_empresas)} ações')
print(f'A média de PL da carteira é {int(sum(pl_empresas)/len(nome_empresas))}')
print(f'A média de ROE da carteira é {roe_medio}')
print(f'A empresa mais barata é {empresa_menor_pl}')

if len(nome_empresas) <= 3:
    print('Sua carteira está mal diversificada, é recomendado ter mais de 3 empresas')