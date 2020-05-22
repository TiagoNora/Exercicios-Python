#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o valor do produto: '))
precof = produto - (produto * 0.05)
print(f'Um produto com valor de {produto} euros fica a {precof} euros ápos um desconto de 5%.')