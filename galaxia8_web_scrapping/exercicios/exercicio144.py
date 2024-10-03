from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from io import StringIO


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes')

WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/app-root/app-root/div/div/main/dynamic-comp/div/div[2]/div[1]/div/iframe")))

botao_pesquisar = driver.find_element("xpath", '/html/body/div/form/div/input')

driver.execute_script("arguments[0].click();", botao_pesquisar)

tabela = driver.find_element("xpath", '/html/body/div/table')

html_tabela = tabela.get_attribute('outerHTML')

cotacao_dolar = pd.read_html(StringIO(html_tabela), decimal=',')[0]

driver.quit()

cotacao_dolar = cotacao_dolar.droplevel(level = 0, axis = 1)
cotacao_dolar = cotacao_dolar.dropna(axis = 1).drop(18, axis = 0)
pd.set_option('display.max_rows', None)

print(cotacao_dolar)
