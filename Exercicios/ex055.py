maiorpeso = 0
menorpeso = 0
for x in range(1, 6):
    peso = float(input(f'Digite o peso da {x}ª pessoa: '))
    if x == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'Maior peso: {maiorpeso}')
print(f'Menor peso: {menorpeso}')