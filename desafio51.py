numero = int(input('Digite o número inicial da progressão aritimética: '))
razao = int(input('Digite a razão da progressão aritimética: '))
decimo = numero + (10 -1) * razao

for cont in range(numero, decimo + razao, razao):
    print('{}'.format(cont), end = ' ')
    