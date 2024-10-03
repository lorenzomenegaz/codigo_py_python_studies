try:

    nome_usuario = str(input('Digite seu nome: ')).title()
    idade_usuario = int(input('Digite sua idade: '))

    if idade_usuario < 0:
        while True:
            print('Digite uma idade válida')
            idade_usuario = int(input('Digite sua idade: '))
            if idade_usuario > 0:
                break

    idade_posterior = idade_usuario + 3

    print(f'Parabéns por estar participando do codigo.py {nome_usuario}, com {idade_posterior} você sera muito bom(a) em Python!')

except ValueError:

    print('Digite um valor válido')

finally:
    print('*'*35)
    print('Continue focado em seu aprendizado!')
    print('*'*35)
    