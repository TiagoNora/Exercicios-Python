#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
s = - 999
cont = -1
n = 0
while n != 999:
    n = int(input('Digite um numero (999 condiçao para parar): '))
    cont += 1
    s += n
print(f'Digitou {cont} numeros!')
print(f'A soma entre todos os numeros digitados é {s}!')

