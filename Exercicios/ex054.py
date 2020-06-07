#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
anoatual = datetime.datetime.today().year
maior = 0
menor = 0
for x in range(1,8):
    ano = int(input(f'Digite o ano de nascimento da {x}º pessoa: '))
    idade = anoatual - ano
    if 18 <= idade:
        maior += 1
    else:
        menor += 1
print(f'Maiores de idade: {maior}')
print(f'Menores de idade: {menor}')