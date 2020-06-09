#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

import time
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

escolha = 0
while escolha != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Digite a sua escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}!')
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f'A multiplicaçao entre {n1} e {n2} é {multiplicar}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O número {n1} é maior do que o número {n2}')
        elif n1 == n2:
            print(f'O número {n1} é igual ao número {n2}')
        else:
            print(f'O número {n1} é menor do que o número {n2}')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segunfo numero: '))
    elif escolha == 5:
        print('Encerrando o programa!')
        time.sleep(2)
    else:
        print('Tente outra vez!')
    print('----'*10)
print('Programa encerrado!')