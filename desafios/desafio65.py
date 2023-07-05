total = 0
continua = ''
contador = 0
maior = 0
menor = 0

print('')

while continua != 'n':
    numero = int(input('Digite um número: '))
    
    if contador == 0:
        maior = numero
        menor = numero
    
    if numero > maior:
        maior = numero
    
    if numero < menor:
        menor = numero
    
    total += numero
    contador += 1
    continua = str(input('Deseja continuar (s/n)? ')).strip().lower()

media = total / contador

print('')
print('A média entre os valores digitados é {:.2f}, o valor maior {}, o valor menor {}'.format(media, maior, menor))
print('')
