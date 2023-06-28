matriz = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = input ('digite um número: ')
    
        while not matriz[linha][coluna].isdigit():
            print('')
            print('Digito invalido! Por favor digite somente números inteiros!')
            matriz[linha][coluna] = input('Digite um numero: ')

print('')
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^8}]', end = '')
    print()

print('')
    