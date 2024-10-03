lista_base = ['Vale', 'Weg', 'Renner', 'Bradesco']
lista_base = list(['Vale', 'Weg', 'Renner', 'Bradesco'])
print(lista_base)

lista_vazia = []
lista_tipos_diferentes = ['flamengo', 8, 'campeonatos brasileiros']

lista_dentro_de_listas = [[1,2,3], [4,5,6], [7,8,9]] #matriz 3x3

for lista in lista_dentro_de_listas:
    for item in lista:
        print(item, end=' ')
    print()

#adicionando novos itens no final da lista
lista_sinais = []

lista_sinais.append('bom dia')
lista_sinais.append('boa tarde')
lista_sinais.append('boa noite')
lista_sinais.append('good morning')
lista_sinais.append('good afternoon')
lista_sinais.append('good evening')
lista_sinais.append('good night')
print(lista_sinais)

#selecionando elementos na lista
print(lista_sinais[0])
print(lista_dentro_de_listas[0][2])

#selecionando vários elementos
print(lista_sinais[0:2])
print(lista_sinais[1:])
print(lista_sinais[:3])
print(lista_sinais[-2:])

#alterando elementos
lista_sinais[0] = 'olá'
print(lista_sinais)

#alterando elementos em posições desejadas
lista_sinais.insert(2, 'compra até acabar o caixa')

#remove elementos da lista
lista_sinais.remove('compra até acabar o caixa')

#remove uma posição específica
del lista_sinais[0]

#verifica se um elemento está na lista

verificando = 'boa noite' in lista_sinais
verificando2 = 'olá' not in lista_sinais

#junção de listas

lista1 = [0,1,2,3]
lista2 = [5,6]

lista_final = lista1 + lista2 #listas são vetores! isso é feito através do pacote numpy e teremos um vetor

#ordenação de listas

lista_ordenada = [56, 51, 12, 8, 1]
lista_ordenada_crescente = sorted(lista_ordenada)
lista_ordenada_decrescente = sorted(lista_ordenada, reverse=True)

#extraindo o tamanho de uma lista
print(len(lista_ordenada))

#extraindo valores máximos, médios e minímos de uma lista
print(max(lista_ordenada))
print(min(lista_ordenada))
print(sum(lista_ordenada)/len(lista_ordenada))