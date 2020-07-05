#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
for x in range(1,8):
    n = int(input(f'Digite o {x}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Valores Pares: {sorted(lista[0])} ')
print(f'Valores Ímpares: {sorted(lista[1])} ')