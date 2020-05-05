cidade = str(input('Digite o nome da sua cidade: '))
dividido = cidade.split()
print(f'{cidade} tem "PORTO" no nome: {"PORTO" in dividido[0].upper()}')