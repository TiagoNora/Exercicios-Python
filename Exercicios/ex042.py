#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
s1 = int(input('Digite  valor do primeiro segmento: '))
s2 = int(input('Digite  valor do segundo segmento: '))
s3 = int(input('Digite  valor do terceiro segmento: '))
if s1 > 0 and s2 > 0 and s3 > 0:
    if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
        print('Com os segmentos dados é possivel formar um triangulo: ', end='')
        if s1 == s2 == s3:
            print('EQUILÁTERO')
        elif s1 != s2 != s3 != s1:
            print('ESCALENO!')
        else:
            print('ISÓSCELES!')

    else:
        print('Com esses segmentos não dá para criar um triângulo')

else:
    print('ERRO.Tente outra vez!')