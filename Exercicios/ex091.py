# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6)}
for k, n in jogadores.items():
    print(f'{k} sorteou o numero {n}')
    sleep(1)
print('-' * 30)
print(f'{"Ranking":>18}')
print('-' * 30)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(rank):
    print(f'{i + 1}º lugar : {v[0]} com {v[1]}')
    sleep(1)
print('-' * 30)