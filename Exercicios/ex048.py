#Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três , que sejam impares e que se encontram no intervalo de 1 até 500.
cont = 0
s = 0
for x in range(1, 501):
    if x % 3 == 0:
        if x % 2 != 0:
            cont += 1
            s += x
print(f'Foram encontrados {cont} valores multiplos de 3.')
print(f'As somas dos {cont} valores é {s}')