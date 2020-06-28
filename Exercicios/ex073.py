#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Portugues de Futebol,
#na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o Fc Porto.

clubes = ('FC Porto', 'Benfica','Sporting','Braga','Famaição','Rio Aves',
          'Vitória SC','Santa Clara','Moreirense','Boavista','Gil Vicente','Paços Ferreira',
          'Vitória Fc','Belenenses','Tondela','Marítimo','Portimonense','Aves')

print(f'Os primeiros clubes são : {clubes[:5]}')
print(f'Os últimos 4 colocados são : {clubes[-4:]}')
print(f'Lista em ordem alfabética : {sorted(clubes)}')
print(f'O Fc Porto está na {clubes.index("FC Porto") + 1}º posição.')