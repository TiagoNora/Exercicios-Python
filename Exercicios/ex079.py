#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Número já presente na lista!')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar[S/N]: ')).upper().strip()
    if resposta == 'N':
        break
lista.sort()
print(f'Valores digitados por ordem crescente: {lista}.')