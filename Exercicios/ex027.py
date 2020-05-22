#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o seu nome completo: ')).split()
print(f'O seu primeiro nome é {nome[0]}.')
print(f'O seu último nome é {nome[-1]}.')
