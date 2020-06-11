#Escreva um programa que leia um número N inteiro qualquer
#e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

termos = int(input('Digite o numero de termos que quer mostrar: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} > {t2}', end= '')
while cont <= termos:
    t3 = t1 + t2
    print(f' > {t3}',end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' > Fim')