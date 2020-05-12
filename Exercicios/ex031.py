km = int(input('Qual é a distancia da viagem: '))
if km <= 200:
    valor = km * 0.5
    print(f'Vai ter de pagar {valor} euros.')
else:
    valor = km * 0.45
    print(f'Vai ter de pagar {valor} euros.')