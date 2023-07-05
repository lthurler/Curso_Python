from random import randint

numeros = (randint(0,99), randint(0,99), randint(0,99), randint(0,99), randint(0,99))

print('')
print(f'Os números gerados foram :')
print('')
for numero in numeros:
    print(f'{numero} ', end ='')

print('')
print('')
print(f'O maior valor sorteado foi {max(numeros)}')
print('')
print(f'O menor valor sorteado foi {min(numeros)}')
print('')
