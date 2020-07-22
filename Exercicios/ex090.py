#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média do {aluno["Nome"]}: '))
if aluno['Media'] < 10:
    aluno['Situação'] = 'Reprovado'
if 10 <= aluno['Media'] < 14:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
for k , v in aluno.items():
    print(f'{k} é {v}')