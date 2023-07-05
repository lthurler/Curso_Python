lista = ('Bala', 1.00,
         'Chiclete', 2.00,
         'Chocolate', 5.00,
         'Sorvete', 4.00)

print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 39)

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end = '')
    else:
        print(f'R${lista[posicao]:>6.2f}')

print('-' * 39)