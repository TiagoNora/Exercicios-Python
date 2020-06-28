#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezasseis', 'Dezassete', 'Dezoito', 'Dezanove', 'Vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente outra vez. ',end='')
print(f'0 numero {n} em extenso lê-se {extenso[n]}.')