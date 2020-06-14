#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

while True:
    tabuada = int(input('Qual a tabuada que quer ver: '))
    print('-' * 30)
    if tabuada < 0:
        break
    for x in range(1, 11):
        print(f'{tabuada} * {x} = {tabuada * x}')
    print('-' * 30)
print('Programa encerrado!')