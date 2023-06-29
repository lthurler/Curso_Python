matriz = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
somapar = maior = somacoluna = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = input(f'digite um número para [{linha}, {coluna}]: ')
    
        while not matriz[linha][coluna].isdigit():
            print('')
            print('Digito invalido! Por favor digite somente números inteiros!')
            matriz[linha][coluna] = input(f'digite um número para [{linha}, {coluna}]: ')

print('')
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^8}]', end = '')
        
        if int(matriz[linha][coluna]) %2 == 0:
            somapar += int(matriz[linha][coluna])
    print()

print('')
print(f'A soma dos números pares é: {somapar}')

for linha in range(0,3):
    somacoluna += int(matriz[linha][2])

print(f'A soma dos valores da terceira coluna é: {somacoluna}')

for coluna in range(0,3):
    if coluna == 0:
        maior = int(matriz[1][coluna])
    
    elif int(matriz[1][coluna]) > maior:
        maior = int(matriz[1][coluna])

print(f'O maior valor da segunda linha é: {maior}')
print('')
