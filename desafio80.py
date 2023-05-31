lista_numeros = []

for i in range(0,5):
    print('')
    
    numero = input('Digite um número: ')
    
    while not numero.isdigit():
        print('')
        print('Entrada inválida. Digite somente números')
        numero = input('Digite um número: ')
        print('')
    
    if i == 0 or numero > lista_numeros[-1]:
        lista_numeros.append(numero)
        
    else:
        posicao = 0
        
        while posicao < len(lista_numeros):
            if numero <= lista_numeros[posicao]:
                lista_numeros.insert(posicao, numero)
                break
            posicao += 1

print('')
print(f'Os números digitados foram {lista_numeros}')
print('')
    