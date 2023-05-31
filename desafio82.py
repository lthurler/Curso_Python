lista_numeros = []
lista_par = []
lista_impar = []

while True:
    print('')
    
    numero = input('Digite um número: ')
    
    while not numero.isdigit():
        print('')
        print('Entrada inválida. Digite somente números')
        numero = input('Digite um número: ')
        print('')
    
    lista_numeros.append(numero)    
    
    if int(numero) % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
              
    resposta = str(input("Deseja continuar? (s/n): "))
    print('')
    
    while resposta not in 'sSnN':
        print('')
        print('Resposta inválida! Digite somente (s/S) ou (n/N)')
        print('')
        resposta = str(input("Deseja continuar? (s/n): "))
        print('')
    
    if resposta in 'Nn':        
        break
    
print('')
print(f'Os números digitados foram: {lista_numeros}')
print(f'Dentre esses os pares foram {lista_par}')
print(f'E os impares foram {lista_impar}')
print('')
