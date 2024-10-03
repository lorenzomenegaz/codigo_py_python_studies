from datetime import datetime, date

data = datetime(2023, 1, 1, 12, 58, 30)

print(f'''Dia {data.day}
Mês {data.month}
Ano {data.year}
Hora {data.hour}
Minuto {data.minute}
Segundo {data.second}''')
