def fatorial(numero=1):
    fatorial = 1
    for cont in range(numero, 0 , -1):
        fatorial *= cont
    return fatorial


numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é igual a {fatorial(numero)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')


def par(numero = 0):
    if numero %2 == 0:
        return True
    
    else:
        return False


numero = int(input('Digite um número: '))

if par(numero):
    print('É par!')
    
else:
    print('Não é par!')


