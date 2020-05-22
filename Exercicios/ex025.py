#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o seu nome: '))
print(f'O nome {nome.title()} tem "Silva" no nome: {"SILVA" in nome.upper()}')