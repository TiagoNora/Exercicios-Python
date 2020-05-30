# Crie um programa que faça o computador jogar Pedra, Papel ou tesoura

import random
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Digite a escolha: '))
lista = ['Pedra', 'Papel', 'Tesoura']
escolha = lista[jogador - 1]
pc = random.choice(lista)
print(f'Escolhido pelo pc: {pc}')
print(f'Escolhido pelo jogador: {escolha}')

if 1 <= jogador <= 3:
    if pc == 'Pedra':
        if escolha == 'Pedra':
            print('EMPATE')
        elif escolha == 'Papel':
            print('O JOGADOR VENCEU')
        elif escolha == 'Tesoura':
            print('O PC VENCEU')

    elif pc == 'Papel':
        if escolha == 'Papel':
            print('EMPATE')
        elif escolha == 'Pedra':
            print('O PC VENCEU')
        elif escolha == 'Tesoura':
            print('O JOGADOR VENCEU')

    elif pc == 'Tesoura':
        if escolha == 'Tesoura':
            print('EMPATE')
        elif escolha == 'Pedra':
            print('O JOGADOR VENCEU')
        elif escolha == 'Papel':
            print('O PC VENCEU')
else:
    print('ERRO.TENTE OUTRA VEZ!')
