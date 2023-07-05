numero = 0
valor = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    valor += numero
    contador += 1
    
    if numero == 999:
        contador = contador - 1
        valor = valor - 999
        
print('')
print('Foram digitados {} números e a soma deles é {}'.format(contador,valor))
print('')
