import numpy as np

rentabilidades = np.array([])

rentabilidade = float(input('Digite uma rentabilidade: '))

rentabilidades = np.append(rentabilidades, rentabilidade)

cadastrar_mais = str(input('Deseja cadastrar mais uma rentabilidade? [S/N] ')).lower()

while cadastrar_mais != 'n':
    if cadastrar_mais == 's':
        
        rentabilidade = float(input('Digite uma rentabilidade: '))
        
        rentabilidades = np.append(rentabilidades, rentabilidade)

        cadastrar_mais = str(input('Deseja cadastrar mais uma rentabilidade? [S/N] ')).lower()

    else:
        print('Digite uma resposta válida(S ou N)')
        cadastrar_mais = str(input('Deseja cadastrar mais uma rentabilidade? [S/N] ')).lower()

media = np.mean(rentabilidades)
media = "{:.0%}".format(media)

mediana = np.median(rentabilidades)
mediana = "{:.0%}".format(mediana)

desvio_padrao = np.std(rentabilidades)
desvio_padrao = "{:.0%}".format(desvio_padrao)

maxima, minima = np.max(rentabilidades), np.min(rentabilidades)
maxima, minima = "{:.0%}".format(maxima), "{:.0%}".format(minima)

print(f'''\nAqui estão as estatísticas das rentabilidades:\n
          Média: {media}
          Mediana: {mediana}
          Desvio padrão: {desvio_padrao}
          Rentabilidade máxima: {maxima}
          Rentabilidade mínima: {minima}
''')