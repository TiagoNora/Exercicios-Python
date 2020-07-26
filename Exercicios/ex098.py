from time import sleep


def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p > 0:
        for n in range(i, f + 1, p):
            print(n, end=' ')
            sleep(0.5)
        print('Fim')
    else:
        for n in range(i, f - 1, p):
            print(n, end=' ')
            sleep(0.5)
        print('Fim')


contador(1, 10, 1)
contador(10, 0, -1)

print('-=' * 30)
print('Personalização de contagem')
i = int(input('Ínicio: '))
f = int(input('Final: '))
p = int(input('Passo:: '))
if i < f:
    if p == 0:
        p = 1
else:
    p = -1
contador(i, f, p)
