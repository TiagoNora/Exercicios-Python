#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor do salário: '))
ajuste = salario + (salario * 0.15)
print(f'Um funcionário com um salario de {salario} euros, após um aumento de 15% passa a receber {ajuste} euros ')