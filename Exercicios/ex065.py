#Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

s = 0
cont = 0
maior = 0
menor = 0
resposta = ''
media = 0
while resposta != 'N':
    n = int(input('Digite um numero: '))
    cont += 1
    s += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    media = s / cont
    resposta = str(input('Quer continuar [S/N]: ')).upper().strip()
print(f'Digitou {cont} numeros e media é {media}!')
print(f'Maior numero : {maior}')
print(f'Menor numero : {menor}')