# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# Mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual é a velocidade do carro: '))
if velocidade > 80:
    multa = velocidade - 80
    valor = multa * 7
    print(f'Passou o limite de 80 km/h por a uma velocida de {velocidade} km/h! ')
    print(f'Por isso vai pagar uma multa de {valor} euros')
elif velocidade < 0:
    print('Velocidade inválida!')
else:
    print('Boa viagem! Está dentro do limite de circulação!')