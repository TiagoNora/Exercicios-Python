#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
lista = list()


def sorteia():
    for n in range(0, 5):
        n = randint(0, 11)
        lista.append(n)
    print(f'Lista: ', end='')
    for n in lista:
        print(n, end=' ')


def somaPar():
    s = 0
    sorteia()
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'\nSoma dos numeros pares da lista {lista} é {s}')


somaPar()