lista_base = ['WEGE3', 'PETR4', 'PETR3', 'PCAR3', 'ALPA4']

lista_filtrada = [ticker for ticker in lista_base if ticker.startswith('P')]

print(lista_filtrada)