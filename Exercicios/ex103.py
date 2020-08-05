#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome, golos=0):
    if golos >= 0:
        if golos == 0 or golos > 1:
            return f'O jogador {nome} marcou {golos} golos'
        else:
            return f'O jogador {nome} marcou {golos} golo'
    else:
        return 'ERRO'


nome = str(input('Nome do jogador: '))
golos = str(input('Golos do jogador: '))
if golos.isnumeric():
    golos = int(golos)
else:
    golos = 0
if nome == '':
    nome = '<desconhecido>'

print(ficha(nome, golos))