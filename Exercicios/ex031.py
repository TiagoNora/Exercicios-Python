#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('Qual é a distancia da viagem: '))
if km <= 200:
    valor = km * 0.5
    print(f'Vai ter de pagar {valor} euros.')
else:
    valor = km * 0.45
    print(f'Vai ter de pagar {valor} euros.')