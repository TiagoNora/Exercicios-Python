#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
s = 0
cont = 0
for x in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Foram digitados {cont} numeros pares e a soma deles é {s}')