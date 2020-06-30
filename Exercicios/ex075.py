#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

cont = 0
numeros = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite o último número: ')))
print(f'Os números apresentados foram: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'O primeiro valor 3 foi digitado na {numeros.index(3)}º posição')
for num in numeros:
    if num % 2 == 0:
        cont += 1
if cont > 1 and cont == 0:
    print(f'Dos 4 numeros digitados {cont} são pares.')
else:
    print(f'Dos 4 numeros digitado só 1 dos números é que é par.')