#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

info = dict()
partidas = list()

info['Nome'] = str(input('Nome: '))
total = int(input(f'Quantos jogos o {info["Nome"]} fez: '))
for n in range(0, total):
    partidas.append(int(input(f'        Quantos marcou no {n + 1}º jogo: ')))
info['Golos'] = partidas[:]
info['Total'] = sum(partidas)

print('-' * 60)
print(info)
print('-' * 60)
for k, v in info.items():
    print(f'{k} -- {v}')
print('-' * 60)

print(f'O jogador {info["Nome"]} participou em {total} jogos.')
for c, n in enumerate(info['Golos']):
    print(f'        => No {c + 1}º jogo, fez {n} golos.')
print('-' * 60)