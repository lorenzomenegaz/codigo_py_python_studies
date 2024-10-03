from pandas_datareader import wb 
from datetime import datetime

c02_emissions = wb.download(indicator='EN.ATM.CO2E.KT', 
                      country=['1W'], 
                      start=1990, end=datetime.now())

print(c02_emissions)