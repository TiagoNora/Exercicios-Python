#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
lista = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for x in range(0, 3):
        lista[l][x] = (int(input(f'Digite um valor para [{l},{x}]: ')))
for l in range(0,3):
    for x in range(0, 3):
        print(f'[{lista[l][x]:^7}]', end='')
    print()