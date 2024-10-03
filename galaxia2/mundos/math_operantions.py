num = int(input('Digite um número inteiro qualquer:'))
num2 = int(input('Digite um número inteiro qualquer:'))

soma = num+num2
multiplicar = num*num2
dividir = num/num2
elevar = num**num2
raiz = num**(1/2)
raiz2 = num2**(1/2)
dividir_inteiro = num//num2
resto = num%num2

print('')
print(f'''A soma dos dois números é {soma}\n
A multiplicação é {multiplicar}\n
A divisão é {dividir}\n
O primeiro número elevevado ao segundo chega ao resultado de {elevar}\n
A raiz quadrada do 1º número é {raiz} e do segundo número é {raiz2}\n
A divisão inteira é {dividir_inteiro} e o resto é {resto}''')

string = '-'
string_multiplicada = string*10
print(string_multiplicada)