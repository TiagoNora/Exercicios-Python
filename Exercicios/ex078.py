#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
maior = 0
menor = 0
for cont in range(0,5):
    lista.append(int(input('Digite um número: ')))
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]

print(f'O maior número digitado foi o {maior} e foi encontrado na posiçao {lista.index(maior) + 1}')
print(f'O menor numero digitado foi o {menor} e foi encontrado na posiçao {lista.index(menor) + 1} ')
