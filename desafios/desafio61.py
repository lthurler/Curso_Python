numero = int(input('Digite o número inicial da progressão aritimética: '))
razao = int(input('Digite a razão da progressão aritimética: '))
resultado = numero
contador = 1

while contador != 11:
    print('{} -> '.format(resultado), end = '')
    
    contador +=1
    resultado += razao 
    
print('Fim')   
