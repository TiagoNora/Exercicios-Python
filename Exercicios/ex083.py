#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = list()
cont_esquerda = cont_direita = 0
expressao = str(input('Excreva a sua expressão: '))
lista.append(expressao)
for p in expressao:
    if p == '(':
        cont_esquerda += 1
    if p == ')':
        cont_direita += 1
if cont_esquerda == cont_direita:
    print(f'A expressão {expressao} está correta!')
else:
    print(f'A expressão {expressao} está errada!')