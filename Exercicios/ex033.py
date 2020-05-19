n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3

if n2 > n1 and n3 > n1:
    menor = n1
if n1 > n2 and n3 > n2:
    menor = n2
if n1 > n3 and n2 > n3:
    menor = n3
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')