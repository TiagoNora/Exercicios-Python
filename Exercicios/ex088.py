# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = list()
dados = list()
total = 0
palpites = int(input('Digite o numero de palpites que deseja: '))
while total <= palpites - 1:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in dados:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    dados.append(lista[:])
    lista.clear()
    total += 1
for x, y in enumerate(dados):
    print(f'Jogo {x + 1}: {y}')
    sleep(1)
