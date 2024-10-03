import random

class Empresa:

    ano_atual = 2022 #atributo de classe. Não importa a instância

    def __init__(self, nome, ticker, ano_fundacao, cnpj): #construtor

        self.__nome = nome #atributos da instancia 
        self.ticker = ticker
        self.ano_fundacao = ano_fundacao
        self.cnpj = cnpj

    def tempo_existencia(self): 
    #preciso passar o self pois é um método da instancia. Só é possível executar ele com os atributos da instancia existindo

        self.anos_existencia = self.ano_atual - self.ano_fundacao
        print(f"A empresa existe há {self.anos_existencia} anos!")

    def cnpj_numerico(self): 

        self.cnpj_inteiro = int(self.cnpj.replace("-", "").replace(".", "").replace("/", ""))
        print(f"O CNPJ só com números é {self.cnpj_inteiro}.")

    @classmethod #é referente a classe, não a instancia. Pode ser usado para construir a instancias, quando você só tem parte dos argumentos necessários.
    #vamos supor que você precisa do ano de fundação mas só tem os anos de existencia da empresa. Você pode construir um método de classe q calcula isso pra você.
    def extraindo_empresa_por_ano_existencia(cls, anos_existencia, nome, ticker, cnpj):

        ano_fundacao = cls.ano_atual - anos_existencia
        return cls(nome, ticker, ano_fundacao, cnpj) #tem que ser na mesma ordem do init

        #usado pra quando voce nao tem, ou não quer ter a instancia no primeiro momento
    
    @classmethod
    def extraindo_empresa_corrigindo_ticker(cls, nome, texto_ticker, codigo_ticker, ano_fundacao, cnpj): 

        ticker = texto_ticker + codigo_ticker
        return cls(nome, ticker, ano_fundacao, cnpj)

    @staticmethod #só deixa aqui por organização, uma função normal
    def gera_id():

        id_aleatorio = random.randint(0, 100)
        return id_aleatorio
    
    @staticmethod
    def gera_recomendacao_investimento(): 

        lista_recomendacoes = ['Compra', 'Neutro', 'Venda']
        recomendacao = random.choice(lista_recomendacoes)

        return print(recomendacao)

    #getter e setter servem para tratamento de dados.
    # Nesse mundo iremos tratar o ano da fundação. Assim eu n preciso ficar tratando dado na classe inteira
    #nada mais é que um validador de dados. vai criar só pro que o usuário que pode fazer merda
    #dificilmente você vai usar no dia a dia, principalmente em análise de dados, mas é bom saber que existe.

    #getter
    @property
    def ano_fundacao(self): #pode ser qualquer nome
        return self._ano_fundacao #aqui pode ser qualquer nome

    @ano_fundacao.setter #o mesmo nome do getter
    def ano_fundacao(self, ano): #o importante é a definição aqui, com o atributo sendo o nome da função.

        self._ano_fundacao = int(ano)

    @property 
    def nome(self): 
        return self._nome 

    @nome.setter 
    def nome(self, valor): 

        self._nome = valor.title() 


if __name__ == "__main__": 


    weg = Empresa(nome = "wEg", ticker = "WEGE3", ano_fundacao="1960", cnpj="84.429.695/0001-11")

    print(weg.nome)

    weg.__nome = "Petrobras"

    print(weg.nome)
    print(weg.ticker)





#exercicio 115: Crie um Getter e Setter que trate o atributo "nome" e configure sempre para o formato Title.

