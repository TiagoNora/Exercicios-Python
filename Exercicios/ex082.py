#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = list()
lista_pares = list()
lista_impares = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar[S/N]: ')).upper().strip()
    if resposta == 'N':
        break

lista_pares.sort()
lista_impares.sort()
print(f'Lista completa: {lista}.')
print(f'Lista dos Pares: {lista_pares}.')
print(f'Lista dos Ímpares: {lista_impares}.')