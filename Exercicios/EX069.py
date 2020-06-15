#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

cont_18 = cont_homens = cont_mulheres = 0
while True:
    print('-' * 30)
    print('Registo de uma pessoa: ')
    print('-' * 30)

    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: ')).upper().strip()
    if idade > 18:
        cont_18 += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and 20 <= idade:
        cont_mulheres += 1
    print('-' * 30)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar[S/N]: ')).upper().strip()
    if resposta == 'N':
        break

if cont_18 > 1 or cont_18 == 0:
    print(f'Pessoas com mais de 18 anos: {cont_18} pessoas!')
else:
    print(f'Pessoas com mais de 18 anos: {cont_18} pessoa!')
if cont_homens > 1 or cont_homens == 0:
    print(f'Homens registrados: {cont_homens} homens!')
else:
    print(f'Homens registrados: {cont_homens} homem!')
if cont_mulheres > 1 or cont_mulheres == 0:
    print(f'Mulheres com pelos menos 20 anos: {cont_mulheres} mulheres!')
else:
    print(f'Mulheres com pelos menos 20 anos: {cont_mulheres} mulher!')