import requests
import pandas as pd
import json
from pprint import pprint


url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'

response = requests.get(url)
data = json.loads(response.text)

lista_df = []

for informacoes in data[0]['res']: 

    df = pd.DataFrame(informacoes, index = [0])
    
    lista_df.append(df)
    
rankings_nomes = pd.concat(lista_df, ignore_index = True)

print(rankings_nomes)