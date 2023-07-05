par = []
impar = []
valor = 0

for cont in range(1,8):
    valor = input(f'Digite o {cont}º numero: ')
    
    while not valor.isdigit():
        print('')
        print('Digito invalido! Por favor digite somente números inteiros!')
        valor = input('Digite um numero: ')
    
    if int(valor)%2 == 0:
        par.append(valor)
    
    else:
        impar.append(valor)

par.sort
impar.sort

print('')
print (f'Os valores pares são: {par} e os impares são {impar}')
print('')
