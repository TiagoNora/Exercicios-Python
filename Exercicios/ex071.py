#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de 50€, 20€, 10€ e 1€.

cont50 = cont20 = cont10 = cont1 = 0

dinheiro = int(input('Digite o valor que quer tirar: '))
while True:
    while dinheiro >= 50:
        cont50 += 1
        dinheiro -= 50
    while dinheiro >= 20:
        cont20 += 1
        dinheiro -= 20
    while dinheiro >= 10:
        cont10 += 1
        dinheiro -= 10
    while dinheiro >= 1:
        cont1 += 1
        dinheiro -= 1
    if dinheiro == 0:
        break

if cont1 > 0:
    print(f'{cont1} cédula de 1€!')
if cont10 > 0:
    print(f'{cont10} cédula de 10€!')
if cont20 > 0:
    print(f'{cont20} cédula de 20€!')
if cont50 > 0:
    print(f'{cont50} cédula de 50€!')



