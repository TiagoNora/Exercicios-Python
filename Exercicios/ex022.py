#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome: ')).strip()
separado = nome.split()
print(f'O seu nome em maiúsculas é {nome.upper()}')
print(f'O seu nome em minúsculas é {nome.lower()} ')
print(f'O seu nome tem {len(nome) - nome.count(" ") } letras ')
print(f'O seu primeiro nome é {separado[0]} e tem {len(separado[0])} letras')
