# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

cont = 0

while True:
    bot = random.randint(0, 10)
    jogador = int(input('Digite um número:'))
    total = bot + jogador
    resposta = ' '
    while resposta not in 'PI':
        resposta = str(input('Par ou Ímpar[P/I]: ')).upper().strip()
    print('-' * 30)
    print(f'Jogador: {jogador}', end=' ')
    print(f'Pc: {bot}')
    print(f'Soma: {total} ')
    print('Par' if total % 2 == 0 else 'Ímpar')
    print('-' * 30)
    if resposta == 'P':
        if total % 2 == 0:
            cont += 1
            print('Venceu!')
        else:
            print('Perdeu!')
            break
    if resposta == 'I':
        if total % 2 == 1:
            cont += 1
            print('Venceu!')
        else:
            print('Perdeu!')
            break
    print('-+' * 15)
print(f'Ganhou  {cont} vezes!')
