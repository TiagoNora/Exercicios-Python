#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
s = int(input('Digite o salario do funcionario: '))
if s > 0:
    if s <= 1250:
        snovo = s * 1.15
        print(f'O funcionario que tem um salario de {s} euros passa a ganhar {snovo} euros.')
    elif s > 1250:
        snovo = s * 1.10
        print(f'O funcionario que tem um salario de {s} euros passa a ganhar {snovo} euros.')
else:
    print('Tente outra vez!')