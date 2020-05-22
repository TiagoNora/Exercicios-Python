#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
n = float(input('Digite um numero real: '))
nr = math.trunc(n)
print(f'O número real de {n} é {nr}')