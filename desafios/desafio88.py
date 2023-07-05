from random import randint

lista = list()
jogos = list()
total = 1
quantidade = input('Quantos jogos você quer fazer? ')

while not quantidade.isdigit():
    print('')
    print('Digito invalido! Por favor digite somente números inteiros!')
    quantidade = input('Quantos jogos você quer fazer? ')
    
while total <= int(quantidade):
    contador = 0
    
    while True:
        numero = randint(1, 60)
        
        if numero not in lista:
            lista.append(numero)
            contador += 1
        
        if contador >= 6:
            break
        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
    
if int(quantidade) == 1:
    print('')
    print('*' *4, f'Sorteando 1 jogo', '*' *4)
    print('')
else:
    print('')
    print('*' *4, f'Sorteando {int(quantidade)} jogos', '*' *4)
    print('')
    
for index, listas in enumerate(jogos):
    print(f'jogo{index+1}: {listas}')

print('')
   