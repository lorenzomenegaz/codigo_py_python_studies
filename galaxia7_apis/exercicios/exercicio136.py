import requests
import pandas as pd
from pprint import pprint


pular = 0

lista_df_moedas_comemorativas = []

while True:
    
    url_base = f'''https://olinda.bcb.gov.br/olinda/servico/mecir_moedas_comemorativas/versao/v1/odata/informacoes_diarias?$top=10000&$skip={pular}&$format=json'''
    
    response_bc = requests.get(url_base)
    
    pular = pular + 10000
    
    json_moedas_comemorativas = response_bc.json()
    
    df_moedas_comemorativas = pd.DataFrame(json_moedas_comemorativas['value'])
    
    lista_df_moedas_comemorativas.append(df_moedas_comemorativas)
    
    if len(json_moedas_comemorativas['value']) < 1:
        
        break
        
moedas_comemorativas = pd.concat(lista_df_moedas_comemorativas)

print(moedas_comemorativas[moedas_comemorativas['Quantidade'] < 100])