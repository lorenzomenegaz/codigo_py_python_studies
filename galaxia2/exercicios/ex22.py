graus_celsius = float(input('Digite a temperatura em ºC: '))

def celsius_to_fahrenheit(graus_celsius):
    
    fahrenheit = graus_celsius * 1.8 + 32

    return fahrenheit

print(f'A conversão foi concluída, o valor encontrado em ºF foi de {celsius_to_fahrenheit(graus_celsius= graus_celsius)}')
