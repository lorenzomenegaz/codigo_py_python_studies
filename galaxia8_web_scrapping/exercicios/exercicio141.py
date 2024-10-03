import requests 
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd

response = requests.get('https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o_(2022)')

soup = BeautifulSoup(response.text, 'html.parser')

tabela = soup.find("table", {'class': ['wikitable', 'sortable']})

df = pd.read_html(str(tabela))

pprint(df)