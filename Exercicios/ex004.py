#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print(f'{a} é um ', type(a))
print(f'{a} tem espaços: ', a.isspace())
print(f'{a} é alfanumerico:', a.isalnum())
print(f'{a} é um número: ', a.isnumeric())
print(f'{a} é alfabético: ', a.isalpha())
print(f'{a} é minusculo: ', a.islower())
print(f'{a} é maisculo: ', a.isupper())