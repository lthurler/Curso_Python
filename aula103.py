def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')


nome = input('Nome do jogador: ')
gols = input('Numero de gols: ')

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    ficha(gol = gols)

else:
    ficha(nome, gols)
