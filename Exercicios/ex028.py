import random
jogador = int(input('Digite um numero entre 0 e 5: '))
pc = random.randint(0, 5)
if jogador == pc:
    print('Ganhou!')
else:
    print('Perdeu')