#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
anoatual = datetime.datetime.today().year
anon = int(input('Digite o seu ano de nascimento: '))
idade = anoatual - anon
print(f'Quem nasceu em {anon} tem {idade} em {anoatual}')
if idade == 18:
    print('Tem que ser alistar imediatamente. ')
elif idade > 18:
    d = idade - 18
    ano = anoatual - d
    if d == 1:
        print(f'Já se deveria ter alistado há {d} ano.')
        print(f'Ja se deveria ter alistado no ano {ano}.')
    elif d > 1:
        print(f'Já se deveria ter alistado há {d} anos.')
        print(f'Ja se deveria ter alistado no ano {ano}.')
elif idade < 18:
    d = 18 - idade
    ano = anoatual + d
    if d == 1:
        print(f'Ainda falta {d} ano para o alistamento. ')
        print(f'O alistamento será em {ano}.')
    elif d > 1:
        print(f'Ainda faltam {d} anos para o alistamento. ')
        print(f'O alistamento será em {ano}.')