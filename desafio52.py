numero = int(input('Didite um número: '))
divisoes = 0

for cont in range(1, numero + 1):
    if numero % cont == 0:
        divisoes += 1

if divisoes == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')
    