#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o seu sexo (M/F): ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Tente outra vez! Digite o seu sexo (M/F): ')).upper().strip()

if sexo == 'M':
    print('Sexo Masculino registrado!')
else:
    print('Sexo Feminino registrado!')
