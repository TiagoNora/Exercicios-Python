#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(* num):
    cont = maior_valor = 0
    print('-=' * 30)
    print('Processamento dos dados')
    for n in num:
        print(n, end=' ')
        sleep(0.5)
        if cont == 0:
            maior_valor = n
        else:
            if n > maior_valor:
                maior_valor = n
        cont += 1
    print(f'Foram apresentados {cont} valores')
    print(f'O maior número apresentado foi o {maior_valor}')


maior(1, 2, 3)
