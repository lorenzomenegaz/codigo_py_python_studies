class Empresa:

    def __init__(self, nome, ticker, ano_fundacao, cnpj): #construtor

        self.nome = nome #atributos da instancia 
        self.ticker = ticker
        
        self.ano_fundacao = ano_fundacao
        self.cnpj = cnpj


class Carro:

    def __init__(self, cor, direcao): 

        self.cor_do_carro = cor 
        self.tipo_direcao = direcao


if __name__ == "__main__": #isso aqui serve para fazer testes dentro do próprio código. Só vai rodar quando rodar esse código como main

    empresa_de_motor = Empresa(nome = "WEG", ticker = "WEGE3", ano_fundacao = 1961, cnpj = "07.175.725/0001-60")
    carro_do_nelson = Carro(cor = "Preta", direcao = "Elétrica")

    print(f'Ano de fundação da empresa {empresa_de_motor.nome}: {empresa_de_motor.ano_fundacao}, CNPJ: {empresa_de_motor.cnpj}')
    # print(carro_do_nelson.cor_do_carro)

    #Ex 111: Crie os atributos data de fundação, CNPJ
