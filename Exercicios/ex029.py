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