#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.
lista = list()
cont1 = cont2 = 0
print('-' * 70)
while True:
    nome = str(input('Digite o nome: '))
    n1 = int(input('Digite a primeira nota: '))
    n2 = int(input('Digite a segunda nota: '))
    print('-' * 70)
    m = (n1 + n2) / 2
    lista.append([nome, [n1, n2], m])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuara a introduzir valores [S/N]: ')).strip().upper()
    print('-' * 70)
    if resposta == 'N':
        break
print(f'{"Nº":<10} {"NOME":<30} {"MÉDIA":^10}')
for x, y in enumerate(lista):
    print(f'{x:<10}{y[0]:<30}{y[2]:^10}')
print('-' * 70)
while True:
    if cont1 == 0:
        opcao = ' '
        while opcao not in 'SN':
            opcao = str(input('Quer vizualizar as notas de algum aluno[S/N]: ')).strip().upper()
        print('-' * 70)
        if opcao == 'N':
            break
        else:
            cont1 += 1
    else:
        if cont2 == 0:

            escolha = int(input('Digite o indice do aluno que pretende ver as notas: '))
            print(f'O/a aluno/a chamado/a {lista[escolha][0]} teve as seguintes notas: {lista[escolha][1]}')
            cont2 += 1
        else:
            print('-' * 70)
            retorno = ' '
            while retorno not in 'SN':
                retorno = str(input('Deseja continuar[S/N]: ')).strip().upper()
            print('-' * 70)
            if retorno == 'N':
                break
            escolha = int(input('Digite o indice do aluno que pretende ver as notas: '))
            print(f'O/a aluno/a chamado/a {lista[escolha][0]} teve as seguintes notas: {lista[escolha][1]}')
