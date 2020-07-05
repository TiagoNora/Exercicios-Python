# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

lista = list()
dados = list()
cont = 0
lista_mais100 = list()
lista_menos100 = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    cont += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar[S/N]: ')).upper().strip()
    if resposta == 'N':
        break
for p in lista:
    if p[1] >= 100:
        lista_mais100.append(p[0])
    else:
        lista_menos100.append(p[0])
print(f'Foram registradas {cont} pessoas!')
print(f'Pessoas com mais peso: {lista_mais100}')
print(f'Pessoas com menos peso: {lista_menos100}')
