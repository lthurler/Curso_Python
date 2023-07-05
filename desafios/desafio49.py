numero = int(input('Digite um número para mostra a tabuada do mesmo: '))

print('-'*12)

for count in range (1, 11):    
    print('{} x {:2} = {}'.format(numero, count, numero*count))

print('*'*12)
        