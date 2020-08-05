# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, mostrar=False):
    s = 1
    for x in range(n, 0, -1):
        s *= x
        if mostrar:
            print(x, end=' ')
            if x > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return s


valor_fatorial = int(input('Digite a fatorial que deseja: '))
resposta = ' '
while resposta not in 'SN':
    resposta = str(input('Quer mostrar o desenvolvimento da fatorial[S/N]: ')).upper().strip()
if resposta == 'S':
    valor_logico = True
else:
    valor_logico = False
print('-=' * 30)
print(fatorial(valor_fatorial, valor_logico))