import requests
import pandas as pd
from pprint import pprint


skip = 0

lista_df_moedas_comemorativas = []

while True: 
    
    url_base = f'''https://olinda.bcb.gov.br/olinda/servico/mecir_moedas_comemorativas/versao/v1/odata/informacoes_diarias?$top=10000&$skip={skip}&&$format=json'''                    
        
    response = requests.get(url_base)
        
    skip += 10000

    json_moedas_comemorativas = response.json()

    df_moedas = pd.DataFrame(json_moedas_comemorativas['value'])
    
    lista_df_moedas_comemorativas.append(df_moedas)
    
    if len(json_moedas_comemorativas['value']) < 1:
        
        break
    
base_completa = pd.concat(lista_df_moedas_comemorativas)

pprint(base_completa)