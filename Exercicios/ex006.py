#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n)
print(f'O dobro do número {n} é {dobro}')
print(f'O triplo do número {n} é {triplo}')
print(f'A raiz quadrada do número {n} é {raiz}')
