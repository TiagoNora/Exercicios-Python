#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
from time import sleep


def contador(i, f, p):
    print('-=' * 30)
    if f > i and p > 0 or i > f and p < 0:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        if p > 0:
            for n in range(i, f + 1, p):
                print(n, end=' ')
                sleep(0.5)
            print('Fim')
        else:
            for n in range(i, f - 1, p):
                print(n, end=' ')
                sleep(0.5)
            print('Fim')
    else:
        print('Contador impossivel de ser realizado')


contador(1, 10, 1)
contador(10, 0, -1)

print('-=' * 30)
print('Personalização de contagem')
i = int(input('Ínicio: '))
f = int(input('Final: '))
p = int(input('Passo:: '))
if p == 0:
    if i < f:
        p = 1
    else:
        p = -1
contador(i, f, p)
