inteiro = int(1)
flutuante = float(1.1)
string = str('codigo.py')
boolean = bool(True or False)

verificar_tipo_inteiro = type(inteiro)
verificar_tipo_flutuante = type(flutuante)
verificar_tipo_string = type(string)
verificar_tipo_boolean = type(boolean)

tipos = [
    verificar_tipo_inteiro,
    verificar_tipo_flutuante,
    verificar_tipo_string,
    verificar_tipo_boolean
]

print(tipos)

converter_tipo_objeto = str(inteiro)