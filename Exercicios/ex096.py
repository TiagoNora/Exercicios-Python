#Faça um programa que tenha uma função chamada área()
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(a1, a2):
    a = a1 * a2
    print(f'A área de um terreno {a1}x{a2} é de {a}m2.')


area(float(input('Largura: ')), float(input('Comprimento: ')))