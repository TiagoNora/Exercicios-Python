#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
mais_velho = 0
nome_velho = ''
soma_idades = 0
cont = 0
for x in range(1, 5):
    nome = str(input(f'Digite o nome da {x}ª pessoa: '))
    idade = int(input(f'Digite a idade da {x}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {x}ª pessoa(M/F):  ')).upper()
    soma_idades += idade
    if x == 1 and sexo == 'M':
        mais_velho = idade
        nome_velho = nome
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        cont += 1

media = soma_idades /4
print(f'A média das idades é {media} anos! ')
print(f'O homem mais velho deste grupo chama-se {nome_velho} e tem {mais_velho} anos!')
if cont == 1:
    print(f'Neste grupo existe {cont} mulher com menos de 20 anos!')
else:
    print(f'Neste grupo existem {cont} mulheres com menos de 20 anos!')