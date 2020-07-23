#Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

info = dict()
partidas = list()
lista = list()

while True:
    info.clear
    info['Nome'] = str(input('Nome: ')).capitalize()
    total = int(input(f'Quantos jogos o {info["Nome"]} fez: '))
    for n in range(0, total):
        partidas.append(int(input(f'        Quantos marcou no {n + 1}º jogo: ')))
    info['Golos'] = partidas[:]
    info['Total'] = sum(partidas)
    partidas.clear()
    lista.append(info.copy())
    opcao = ' '

    while opcao not in 'SN':
        opcao = str(input('Quer continuar[S/N]: ')).strip().upper()
        if opcao in 'SN':
            break
        if opcao not in 'SN':
            print('ERRO!', end=' ')
    if opcao == 'N':
        break

print('cod',end=' ')
for k in info.keys():
    print(f'{k:<15}',end='')
print()
for x, y in enumerate(lista):
    print(f'{x:>3}', end=' ')
    for d in y.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    escolha = ' '
    while escolha >= 0:
        escolha = int(input('\nQuer mostrar os dados de qual jogador: '))
    if escolha >= len(lista):
        print(f'ERRO!Não existe um jogador com o código {escolha}.')
    else:
        print(f'-- Dados de {lista[escolha]["Nome"]}:')
        for c, n in enumerate(lista[escolha]['Golos']):
            print(f'        => No {c + 1}º jogo, fez {n} golos.')
        opcao1 = ' '
        while opcao1 not in 'SN':
            opcao1 = str(input('Quer continuar[S/N]: ')).strip().upper()
            if opcao1 in 'SN':
                break
            if opcao1 not in 'SN':
                print('ERRO!', end=' ')
        if opcao1 == 'N':
            break
