jogadores = []
jogador = {}

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Quantas partidas jogou? '))
    jogador['gols'] = []
    jogador['total_gols'] = 0

    for index in range(1, jogador['partidas']+1):
        jogador['gols'].append(int(input(f'Quantos gols na {index}ª partida? ')))
            
    for index, valor in enumerate(jogador['gols']):
        jogador['total_gols'] += valor
        
    jogadores.append(jogador.copy())
    
    resposta = str(input("Deseja continuar? (s/n): "))
        
    print()
    
    while resposta not in 'sSnN':
        print()
        print('Resposta inválida! Digite somente (s/S) ou (n/N)')
        print()
        resposta = str(input("Deseja continuar? (s/n): "))
        print()
    
    if resposta in 'Nn':        
        break

print()

print('Cod ', end='')
for campo in jogador.keys():
    print(f'{campo:<15}', end='')
print()
print('-' *54)    

for chave, valor in enumerate(jogadores):
    print(f'{chave:>2} ', end='')
    for valores in valor.values():
        print(f'{str(valores):<15}', end='')    
    print()
print('-' *54)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    
    if busca == 999:
        break
    
    if busca > len(jogadores):
        print(f'Não existe jogador com código {busca}')
        print()
    
    else:
        print(f'--- Jogador {jogadores[busca]["nome"]:}')
        for index,gols in enumerate(jogadores[busca]['gols']):
            print(f'No {index+1}º jogo fez {gols} gols')
    print('-' *40)

print()
    