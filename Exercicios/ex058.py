#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random

bot = random.randint(0, 10)
print(bot)
palpite = int(input('Digite o seu palpite: '))
palpites = 1
if 0 <= palpite <= 10:
    if palpite < bot:
        print('Digite um numero maior!')
    elif palpite > bot:
        print('Digite um numero menor')
    while palpite != bot:
        palpite = int(input('Digite o seu palpite: '))
        palpites += 1
        if palpite < bot:
            print('Digite um numero maior!')
        elif palpite > bot:
            print('Digite um numero menor')
    print(f'Numero esolhido pelo computador {bot} !')
    print(f'Após {palpites} tentativas acertou !')
else:
    print('Digite um numero válido!')
