#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
tabuada = int(input('Digite um numero para ver a tabuada respetiva: '))
for x in range(1,11):
    print(f'{tabuada} x {x} = {tabuada * x}')