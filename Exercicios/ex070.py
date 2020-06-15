#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de 1000€.
#C) qual é o nome do produto mais barato.

total = cont = cont1000 = menor = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    print('-' * 30)
    resposta = ''
    cont += 1
    total += preco
    if preco > 1000:
        cont1000 += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar[S/N]: ')).upper().strip()
    if resposta == 'N':
        break
    print('-' * 30)
print(f'Total gasto: {total} euros!')
if cont1000 > 1 or cont1000 == 0:
    print(f'Produtos que custam mais de 1000€ : {cont1000} produtos!')
else:
    print(f'Produtos que custam mais de 1000€ : {cont1000} produto!')
print(f'Nome do produto mais barato : {barato} com um valor de {menor} euros!')