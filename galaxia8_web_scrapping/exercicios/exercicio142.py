from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

data_di = "03/02/2023"
mercadoria = 'DI1'

url = f'''
https://www2.bmf.com.br/pages/portal/bmfbovespa/boletim1/SistemaPregao1.asp?pagetype=pop&caminho=Resumo%20
Estat%EDstico%20-%20Sistema%20Preg%E3o&Data={data_di}&Mercadoria={mercadoria}
'''
print(url)

driver.get(url)

driver.implicitly_wait(3)

local_tabela = '''
/html/body/div/div[2]/form[1]/table[3]/tbody/tr[3]/td[3]/table
'''

local_indice = '''
/html/body/div/div[2]/form[1]/table[3]/tbody/tr[3]/td[1]/table
'''

elemento = driver.find_element("xpath", local_tabela)

elemento_indice = driver.find_element("xpath", local_indice)

html_tabela = elemento.get_attribute('outerHTML')
html_indice = elemento_indice.get_attribute('outerHTML')

tabela = pd.read_html(html_tabela)[0]
indice = pd.read_html(html_indice)[0]

driver.quit()

tabela.columns = tabela.loc[0]

tabela = tabela['ÚLT. PREÇO']

tabela = tabela.drop(0, axis = 0)

indice.columns = indice.loc[0]

indice_di = indice['VENCTO']

indice = indice.drop(0, axis = 0)

tabela.index = indice['VENCTO']

tabela = tabela.astype(int)

tabela = tabela[tabela != 0]

tabela = tabela/1000

legenda = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    index = ['F', 'G', 'H', 'J', 'K', 'M', 'N', 'Q', 'U', 'V', 'X', 'Z'])

lista_datas = []

for indice in tabela.index:

    letra = indice[0]
    
    legenda["F"]
    ano = indice[1:3]

    mes = legenda[letra]

    data = f"{mes}-{ano}"

    data = datetime.strptime(data, "%b-%y")

    lista_datas.append(data)


tabela.index = lista_datas  

print(tabela)