#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 10.0: REPROVADO
#- Média entre 10 e 13.9: RECUPERAÇÃO
#- Média 14 ou superior: APROVADO
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota '))
m = (n1 + n2) / 2
if 0 <= m <= 20:
    if m < 10:
        print(f'Com media de {m:.1f} o seu status é \033[30;41mREPROVADO\033[m .')
    elif 10 <= m < 14:
        print(f'Com media de {m:.1f} o seu status é \033[30;43mRECUPERAÇÃO\033[m .')
    elif 10 <= m <= 20:
        print(f'Com media de {m:.1f} o seu status é \033[30;42mAPROVADO\033[m .')
else:
    print('Tente outra vez!')