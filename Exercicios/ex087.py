#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
lista = [[0,0,0], [0,0,0], [0,0,0]]
s_pares = s_terceira = maior = cont = 0
print('-' * 30)
for l in range(0,3):
    for x in range(0, 3):
        lista[l][x] = (int(input(f'Digite um valor para [{l},{x}]: ')))
        if lista[l][x] % 2 == 0:
            s_pares += lista[l][x]
for l in range(0,3):
    for x in range(0, 3):
        print(f'[{lista[l][x]:^7}]', end='')
    print()
print('-'* 30)
s_terceira = lista[0][2] + lista[1][2] + lista[2][2]
for p in lista[1]:
    if cont == 0:
        maior = p
    else:
        if p > maior:
            maior = p
    cont += 1
print(f'A soma dos pares digitados é {s_pares}')
print(f'A soma dos valores terceira coluna é {s_terceira}')
print(f'O maior numero da segunda linha é o numero {maior}')