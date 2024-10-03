# sets tem ordem aleatória alterada sempre
set_teste = {'weg', 'renner', 'c&a', 'SLC agricola'}
set_numero = {1, 4, 5, 8}

#remover duplicatas
lista_duplicada = ['renner', 'weg', 'renner', 'weg']
lista_unica = list(set(lista_duplicada))# vc pode converter listas em set ou tuplas

#adicionando um ao mais elementos a sets
set_numero.add(10)
set_numero.update([20, 25, 60])

# removendo elementos
set_numero.discard(1)

# operações matemáticas de união, interseção, diferença e diferença simétrica
meu_set = {1, 2, 3, 5, 8, 9}
meu_set2 = {1, 4, 5, 6, 8, 11, 12}

# UNIÃO
print(meu_set |  meu_set2)
print(meu_set(meu_set2))

# INTERESEÇÃO(TEM QUE ESTAR NOS DOIS AO MESMO TEMPO)
print(meu_set & meu_set2)
print(meu_set.intersection(meu_set2))

#  DIFERENÇA(SÓ PODE ESTAR PRESENTE O SET 1)
print(meu_set - meu_set2)
print(meu_set.difference(meu_set2))