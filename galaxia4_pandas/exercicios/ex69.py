import pandas as pd
import numpy as np

serie_dados = pd.Series([20, 30, pd.NA, 25, 22, pd.NA, 17])

serie_dados = serie_dados.fillna(0)

retornos = []

for i, dado in enumerate(serie_dados):
    
    if i == 0:
        
        retornos.append(pd.NA)
    
    else:
        
        retorno = serie_dados[i]/serie_dados[i - 1] - 1
        
        retornos.append(retorno)
        
        
serie_retornos = pd.Series(retornos)

serie_retornos = serie_retornos.dropna()

serie_retornos = serie_retornos.replace([-1, np.inf], 0) #sempre pensem em listas quando precisar de mais de 1 elemento

print(serie_retornos)