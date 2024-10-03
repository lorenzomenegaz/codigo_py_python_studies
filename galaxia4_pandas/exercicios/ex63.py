from pandas_datareader import data as pdr 
from datetime import datetime
from pandas_datareader.famafrench import get_available_datasets

get_available_datasets() #Emerging_5_Factors

dados_factor_investing = pdr.get_data_famafrench('Emerging_5_Factors', start = 1990)

print(dados_factor_investing)