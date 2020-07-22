#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
info = dict()

info['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
info['Idade'] = datetime.today().year - nascimento
info['Carteira'] = int(input('Carteira de Trabalho(No caso de não ter digite 0): '))

if info['Carteira'] > 0:
    info['Ano De Contratação'] = int(input('Ano de contratação: '))
    info['Salário'] = int(input('Salário: '))
    info['Reforma'] = (info['Ano De Contratação'] + 35) + info['Idade'] - datetime.today().year
if info['Carteira'] == 0:
    del info['Carteira']
print()
print('-' * 30)
print(f'{"Informação do Trabalhador":^15}')
print('-' * 30)
print()
for k, v in info.items():
    print(f'{k} -- {v}')
print()
print('-' * 30)
