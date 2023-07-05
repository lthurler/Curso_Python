while True:
    numero = int(input('Digite um número para calcular sua tabuada (um número negativo encerra): '))
    
    if numero < 0:
        break
    
    print('')
    
    for cont in range (1, 11):
        print(f' {numero} x {cont} = {numero * cont}')
        
    print('')

print('')   
print('Fim')
print('')
