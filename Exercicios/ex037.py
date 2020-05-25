#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um numero: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
escolha = int(input('Digite a sua escolha: '))
if 0 < escolha < 4:
    if escolha == 1:
        print(f'O numero {n} convertido em binario é {bin(n)[2:]} ')
    if escolha == 2:
        print(f'O numero {n} convertido em octal é {oct(n)} ')
    if escolha == 3:
        print(f'O numero {n} convertido em hexadecimal é {hex(n)} ')

