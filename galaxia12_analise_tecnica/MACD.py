from estrategia import BigStrategy
from indicadores import MakeIndicator
from data_feed import ReadData
from otimizacao_movel import WalkForwardAnalysis

class MACD_estrategia(BigStrategy):

    def __init__(self):
        super().__init__()

    
    def fazendo_indicadores(self):

        self.media_longa = MakeIndicator().media_movel_exponencial(self.dados.fechamento, 26)
        self.media_curta = MakeIndicator().media_movel_exponencial(self.dados.fechamento, 12)

        self.MACD = self.media_longa - self.media_curta

        self.media_MACD = MakeIndicator().media_movel_exponencial(self.MACD, self.parametro1)

        self.lista_indicadores = [self.media_longa, self.media_longa, self.MACD, self.media_MACD]

    def evento(self, data, i):

        if self.MACD[data] >= self.media_MACD[data]:

            #if self.comprado:
            if self.vendido:

                pass

            else:
                # self.vender_cdi()
                # self.compra(inverter=True)
                self.venda(inverter=True)
                self.comprar_cdi()

        elif self.MACD[data] < self.media_MACD[data]:

            #if self.vendido:
            if self.comprado:

                pass

            else:

                # self.venda(inverter = True)
                # self.comprar_cdi()
                self.vender_cdi()
                self.compra(inverter=True)
  

if __name__ == '__main__':

    acao = "PETR4"

    dados = ReadData(

        nome_arquivo= 'cotacoes.parquet',
        tem_multiplas_empresas=True,
        empresa_escolhida=acao,
        nome_coluna_empresas = 'ticker',

        data_inicial = "2010-01-01", 
        data_final = "2021-04-18", 
        
        formato_data = ('%Y-%m-%d'), 

        coluna_data = 0, 
        abertura = 12, 
        minima = 15, 
        maxima = 13, 
        fechamento = 11, 
        volume = 9
    )
    

    walk = WalkForwardAnalysis(estrategia = MACD_estrategia(), class_dados = dados,
                               parametro1= range(3, 15, 3), anos_otimizacao=2, anos_teste=1, 
                               nome_arquivo = f"backtest_2pra1_{acao}_MACD.pdf")

    
    

    walk.run_walk()