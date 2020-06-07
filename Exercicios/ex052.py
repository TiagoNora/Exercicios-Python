#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
n = int(input('Digite um numero: '))
for x in range(1, n+1):
    if n % x == 0:
        cont += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(x, end=' ')

print(f'\n\033[mO numero {n} foi dividido por {cont} vezes')
if cont <= 2:
    print(f'Logo, o numero {n} é primo!')
else:
    print(f'Logo, o numero {n} não é primo')