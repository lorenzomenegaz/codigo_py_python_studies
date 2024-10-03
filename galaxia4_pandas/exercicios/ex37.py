import numpy as np
import pandas as pd

informacoes = {'Cotações': [8.13, 7.94, 8.21],'Volume': [12100, 31298, 91823],'Data': pd.date_range('2023-11-01', periods= 3)}

dataframe = pd.DataFrame(informacoes)

print(dataframe)