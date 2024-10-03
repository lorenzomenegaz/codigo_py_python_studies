from pandas_datareader import data as pdr
from datetime import datetime

dado = "CPIAUCSL"

inicio = "1947-01-01"
final = datetime.now()

dado_fred = pdr.get_data_fred(dado, inicio, final)

print(dado_fred)