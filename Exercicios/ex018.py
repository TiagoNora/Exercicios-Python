# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Dgite o angulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'Para um angulo de {angulo} o seu seno é {seno:.2f} ')
print(f'Para um angulo de {angulo} o seu cosseno é {cosseno:.2f} ')
print(f'Para um angulo de {angulo} a sua tagente é {tangente:.2f} ')
