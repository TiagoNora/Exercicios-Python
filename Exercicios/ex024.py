#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Digite o nome da sua cidade: '))
dividido = cidade.split()
print(f'{cidade} tem "PORTO" no nome: {"PORTO" in dividido[0].upper()}')