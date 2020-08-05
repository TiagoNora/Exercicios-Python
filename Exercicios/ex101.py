#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime


def voto(ano):
    idade = datetime.now().year - ano
    if idade > 0:
        if idade < 18:
            return f'Com {idade} anos: VOTO NEGADO'
        elif 18 <= idade <= 65:
            return f'Com {idade} anos: VOTO OBRIGATÓRIO'
        else:
            return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return 'ERRO'


ano_nascimento = int(input('Qual é o seu ano de nascimento: '))
print(voto(ano_nascimento))