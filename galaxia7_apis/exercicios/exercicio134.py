import requests
import json
import pandas as pd


codigo_ipca = 433
url_banco_central = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_ipca}/dados?formato=json'

response = requests.post(url_banco_central)

print(response)