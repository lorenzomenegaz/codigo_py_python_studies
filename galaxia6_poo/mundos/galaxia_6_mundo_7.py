
'''
Atributo e métodos privados/públicos

Variáveis públicas - Nada
Variáveis protegidas - "_" isso aqui pra muita gente deveria ser suficiente. (ele é publico com um _)
Variáveis privadas - "__" isso aqui não deixa você fazer merda de jeito nenhum

Serve pra método também.

'''

import wget

class Cvm:

    def __init__(self):

        self.site = "http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/"

        self._site = "http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/"

        self.__site = "http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/"


    def pegando_itr(self, ano_arquivo):

        #url = self._site + f"itr_cia_aberta_{ano_arquivo}.zip"

        url = self.__site + f"itr_cia_aberta_{ano_arquivo}.zip" 

        wget.download(url)



baixando_dados = Cvm()

#baixando_dados.site = "et bilu"

#baixando_dados._site = "et bilu"

baixando_dados.__site = "et bilu"

print(baixando_dados.__site)

print(baixando_dados._Cvm__site) #ele vai renomear a variável internamente e pra acessar ela, só assim agora. 

baixando_dados.pegando_itr(2022)


'''
Próximas aulas:

Associação, Agregação, Composição e Herança

'''










