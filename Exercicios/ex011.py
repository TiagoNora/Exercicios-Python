# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Digite a largura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
area = largura * comprimento
l= area / 2
print(f'Para uma parede de {area} m2 é preciso {l} litros.')