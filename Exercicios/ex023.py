#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('Introduza um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhares: {m}')
