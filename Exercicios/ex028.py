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
