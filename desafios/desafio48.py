soma = 0

for count in range (1, 501, 2):
    if count % 3 == 0:
        soma = soma + count
print('A soma de todos os valores multiplos de 3 é {}'.format(soma))
