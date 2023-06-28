jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Quantas partidas jogou? '))
# jogador['gols'] = 0
gols = []
total_gols = 0

for index in range(1, jogador['partidas']+1):
    gols.append(int(input(f'Quantos gols na {index}ª partida? ')))

print()

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')

for index, valor in enumerate(gols):
    print(f'Na partida {index+1} fez {valor} gols')
    total_gols += valor

print()    
print(f'Fez um total de {total_gols} gols')
print()


# for index in range(1, jogador['partidas']+1):
#     gols = int(input(f'Quantos gols na {index}ª partida? '))
#     jogador['gols'] += gols
    
# print()

# for chave, valor in jogador.items():
#     print(f'{chave}: {valor}')

# print()
