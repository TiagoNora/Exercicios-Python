#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite a sua fatorial: '))
c = n
a = 1
while c > 0:
    a *= c
    c -= 1
print(f'A fatorial de {n} é igual a {a}! ')