from math import sqrt
co = float(input('Introduza o cateto oposto do triângulo: '))
ca = float(input('Introduza o cateto adjacente do triângulo: '))
hi = (co ** 2) + (ca ** 2)
hf = sqrt(hi)
print(f'Para um cateto oposto de {co} e um cateto adjacente de {ca} a hipotenusa é de {hf:.2f}')