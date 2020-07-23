# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas +++++
# B) A média de idade +++++
# C) Uma lista com as mulheres +++
# D) Uma lista de pessoas com idade acima da média

from operator import itemgetter

info = dict()
pessoa = list()
cont = soma = 0
while True:
    info.clear()
    info['Nome'] = str(input('Nome: '))

    while True:
        info['Sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
        if info['Sexo'] in 'MF':
            break
        else:
            print('ERRO!')

    info['Idade'] = int(input('Idade: '))

    soma += info['Idade']
    cont += 1
    pessoa.append(info.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar[S/N]: ')).strip().upper()
        if opcao in 'SN':
            break
        if opcao not in 'SN':
            print('ERRO!', end=' ')
    if opcao == 'N':
        break


media = soma / cont
print('-=' * 30)
print(f'Foram registradas {cont} pessoas.')
print(f'A média das pessoas foi {media} anos.')

print('As mulheres registadas foram: ',end='')
for p in pessoa:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}',end=' ')
print('\nPessoas com idade acima da média: ',end='')
for p in pessoa:
    if p['Idade'] > media:
        print(f'{p["Nome"]}',end=' ')
print('-=' * 30)