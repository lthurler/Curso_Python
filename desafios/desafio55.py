maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input('Digite o peso da {} pessoa: '.format(pessoa)))
    
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
print('')
print('O maior peso lido foi de {}kg \nO menor peso lido foi de {}kg'.format(maior, menor))
print('')
    