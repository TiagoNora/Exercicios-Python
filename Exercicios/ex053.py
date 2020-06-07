frase = str(input('Digite a sua frase: ')).upper().strip()
separadas = frase.split()
juntas = ''.join(separadas)
inverso = ''
for letra in range(len(juntas) - 1,-1,-1):
    inverso += juntas[letra]
if letra == frase:
    print('É um palindromo!')
else:
    print('Não é uma palindromo!')
