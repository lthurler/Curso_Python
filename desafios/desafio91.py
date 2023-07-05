from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'jogador1': randint(1,6),
           'jogador2': randint(1,6),
           'jogador3': randint(1,6),
           'jogador4': randint(1,6)}
ranking = list()

print('Sorteio: ')

for chave, valor in jogadas.items():
    print(f'{chave} tirou {valor} no dado')
    sleep(1)

ranking = sorted(jogadas.items(), key = itemgetter(1), reverse=True)

print()

for index, valor in enumerate(ranking):
    print(f'{index+1}º lugar: {valor[0]} tirou: {valor[1]}')
    
print()   
