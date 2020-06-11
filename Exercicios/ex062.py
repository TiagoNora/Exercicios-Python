#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
c = 10
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
cont = 0
while c > 0:
    print(p,end=' ')
    c -= 1
    p += r
    cont += 1
    if c == 0:
        c = int(input('\nQuantos que adicionar mais: '))
print(f'Termos digitados: {cont}')