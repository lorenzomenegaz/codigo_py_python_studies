continuar, continuar_while = True, True
contador = 0
lista_inicial = []

while continuar:

    cotacao = float(input('digite a cotação: '))
    deseja_continuar = str(input('deseja continuar? [S/N] ')).lower()
    lista_inicial.append(cotacao)

    if deseja_continuar == 'n' and contador == 0:
        print('você precisa adicionar mais uma cotação pelo menos')
        contador += 1
        continue
    elif deseja_continuar == 'n' and contador != 0:
        contador += 1
        break
    elif deseja_continuar == 's':
        contador += 1
        continue
    else:
        while continuar_while:
            deseja_continuar = str(input('digite uma resposta válida[S/N] ')).lower()
            if deseja_continuar == 's':
                continuar_while = False
            elif deseja_continuar == 'n' and contador != 0:
                contador += 1
                break
            elif deseja_continuar == 'n' and contador == 0:
                print('você precisa adicionar mais uma cotação pelo menos')
                contador += 1
                continuar_while = False
            else:
                continuar_while = True

dicionario_retornos = {}

def calcula_rentabilidade(lista):

    for i in range(1, len(lista)):

        rentabilidade = lista[i]/lista[i - 1] - 1

        rentabilidade_em_porcentagem = "{:.2%}".format(rentabilidade)

        dicionario_retornos.update({f'Retorno dia {i}': rentabilidade_em_porcentagem})

calcula_rentabilidade(lista=lista_inicial)
print(dicionario_retornos)