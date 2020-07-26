#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print('~' * (len(msg) + 5))
    print(f'  {msg}')
    print('~' * (len(msg) + 5))


escreva('A sua mensagem!')
