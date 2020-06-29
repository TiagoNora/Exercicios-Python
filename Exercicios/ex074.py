#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(0,10) , randint(0,10) , randint(0,10), randint(0,10), randint(0,10) )
numeros_ordenados = sorted(numeros)
print(f'Os números escolhidos foram : {numeros}')
print(f'O menor número foi o {numeros_ordenados[0]}')
print(f'O maior número foi o {numeros_ordenados[4]}')
