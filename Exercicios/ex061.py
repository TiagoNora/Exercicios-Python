#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
p = int(input('Qual é o primeiro termo: '))
r = int(input('Qual é a razão: '))
n = -1
while n <= 10:
    n += 1
    termos = p + (n * r)
    print(termos, end='')
    print(' > ' if -2 < n <= 10 else ' ', end='')