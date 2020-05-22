#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
import datetime
ano = int(input('Qual o ano que quer analisar.Intruduza 0 para analisar o ano atual: '))
if ano != 0:
    anob = calendar.isleap(ano)
    if anob is True:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} não é bissexto')
if ano == 0:
    anoatual = datetime.datetime.now().year
    anoatualb = calendar.isleap(anoatual)
    if anoatualb is True:
        print(f'O ano {anoatual} é bissexto')
    else:
        print(f'O ano {anoatual} não é bissexto')


