# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite o valor do salario do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
salario30 = salario * 0.3
mesesdecompra = anos * 12
pmcasa = casa / mesesdecompra
if salario30 > pmcasa:
    print('Emprestimo aprovado! ')
else:
    print('Emprestimo negado! ')


