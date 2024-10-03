import requests
import json
import pandas as pd


codigo_ipca = 433
url_banco_central = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_ipca}/dados?formato=json'

dados_ipca = requests.get(url_banco_central).json()

df = pd.DataFrame(dados_ipca)

print(df)