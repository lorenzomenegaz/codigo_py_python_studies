import requests
import pandas as pd
import json
from pprint import pprint


paises = 'BR'
indicadores = '77857' #Pessoas com internet

url = f'https://servicodados.ibge.gov.br/api/v1/paises/{paises}/indicadores/{indicadores}'

response = requests.get(url)
data = json.loads(response.text)

lista_dfs = []    
lista_anos = []
lista_valores = []

for informacoes in data[0]['series'][0]['serie']: 
        
        #no lugar desse "0", caso você puxe dois indicadores ao mesmo tempo, vai entrar um outro loop.

        valores = list(informacoes.items())
        lista_anos.append(valores[0][0])
        lista_valores.append(valores[0][1])

df = pd.DataFrame(list(zip(lista_anos,lista_valores)), columns=["Anos", "Brasil"]).dropna()
df = df.set_index("Anos")

print(df)