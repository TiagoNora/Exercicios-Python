#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
jogador = int(input('Digite um numero entre 0 e 5: '))
pc = randint(0, 5)
if 0 <= jogador <= 5:
    if jogador == pc:
        print('Ganhou!')
    elif jogador != pc:
        print('Perdeu!')
else:
    print('Entrada Inválida!.Introduza um numero entre 0 e 5!')
