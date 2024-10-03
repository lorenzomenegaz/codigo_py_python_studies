from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_input_usuario = str(input('Digite uma data no formato brasileiro: '))

data_formatada = datetime.strptime(data_input_usuario, '%d/%m/%Y').date()
dia_anterior = data_formatada - timedelta(days = 1)
ano_seguinte = data_formatada + relativedelta(years = 1)

print(f'Você digitou a data {data_formatada}, um dia anterior é {dia_anterior} e um ano a frente é {ano_seguinte}')