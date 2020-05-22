#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Na frase aparece {frase.count("A")} vezes a letra A.')
print(f'O primeiro A encontra se na posição {frase.find("A") + 1}')
print(f'O último A encontra se na posição {frase.rfind("A") + 1}')