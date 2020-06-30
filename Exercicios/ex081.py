#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar[S/N]: ')).upper().strip()
    if resposta == 'N':
        break
if cont > 0 or cont == 0:
    print(f'Foram digitados {len(lista)} numeros')
else:
    print(f'Foi digitado só um número.')
lista.sort(reverse=True)
print(f'Lista de valores ordenada de forma decrescente: {lista}.')
if 5 not in lista:
    print('O numero 5 não está na lista.')
else:
    print('O número 5 existe na lista')
