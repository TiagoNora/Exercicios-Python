#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
for x in range(0,10):
    print(pt + (x * razao), end=' ')