print('')
valores = (int(input('Digite um número > ')),
           int(input('Digite um número > ')),
           int(input('Digite um número > ')),
           int(input('Digite um número > ')))

print('')
print(f'O número 9 foi digitado {valores.count(9)} vezes.')
print('')

if 3 in valores:
    print(f'O número 3 foi digitado na posição {valores.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
    
print('')
print('Os números pares foram: ', end='')

for numero in valores:
    if numero % 2 == 0:
        print(numero, end =' ')

print('')
        