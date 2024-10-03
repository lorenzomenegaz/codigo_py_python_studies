import re

numero_de_celular = input('Digite seu número de celular incluindo o DDD: ')
padrao = r'^\(?(?:[14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])\)? ?(?:[2-8]|9[0-9])[0-9]{3}\-?[0-9]{4}$'

expressao_regular = re.compile(padrao)

if re.fullmatch(expressao_regular, numero_de_celular):

    print("Seu número de telefone/celular é valido")

else:

    print("Seu número de telefone/celular inválido")
