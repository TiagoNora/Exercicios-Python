#Desenvolva um programa que leia o comprimento de três retas
#E diga ao usuário se elas podem ou não formar um triângulo.
s1 = int(input('Digite  valor do primeiro segmento: '))
s2 = int(input('Digite  valor do segundo segmento: '))
s3 = int(input('Digite  valor do terceiro segmento: '))
if s1 > 0 and s2 > 0 and s3 > 0:
    if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
        print('Com os três segmentos dado dá para formar um triangulo.')
    else:
        print('Com os três segmentos dado não dá para formar um triangulo.')
else:
    print('Tente outra vez.')