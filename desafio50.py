soma = 0

for cont in range(1,7):
    numero = int(input('Digite o {}º número: '.format(cont)))
    if numero %2 == 0:
        soma += numero

print('A soma dos números pares é igual a {}'.format(soma))



