#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
pinicial = int(input('Digite o preço do produto: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão: 20% de juros''')
escolha = int(input('Digite a sua escolha: '))
if 0 <= escolha <= 4:
    if escolha == 1:
        pfinal = pinicial - (pinicial * 0.1)
        print(f'A compra de um porduto de valor {pinicial} euros com a opção {escolha} fica a {pfinal} euros.')
    elif escolha == 2:
        pfinal = pinicial - (pinicial * 0.05)
        print(f'A compra de um porduto de valor {pinicial} euros com a opção {escolha} fica a {pfinal} euros.')
    elif escolha == 3:
        pfinal = pinicial
        parcela = pfinal / 2
        print(f'O produto fica parcelado em 2x de {parcela}.')
        print(f'A compra de um porduto de valor {pinicial} euros com a opção {escolha} fica a {pfinal} euros.')
    elif escolha == 4:
        pfinal = pinicial + (pinicial * 0.2)
        nparcelas = int(input('Por quantas vezes quer parcelar o produto: '))
        parcela = pfinal / nparcelas
        if 3 <= nparcelas:
            print(f'O produto fica parcelado em {nparcelas}x de {parcela}')
            print(f'A compra de um porduto de valor {pinicial} euros com a opção {escolha} fica a {pfinal} euros.')
        else:
            print('ERRO.Tente outra vez!')
else:
    print('ERRO.Tente outra vez!')
