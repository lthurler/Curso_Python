lista_numeros = []

while True:
    print('')
    
    numero = input('Digite um número: ')
    
    while not numero.isdigit():
        print('')
        print('Entrada inválida. Digite somente números')
        numero = input('Digite um número: ')
        print('')
    
    lista_numeros.append(numero)       
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

lista_numeros.sort(reverse=True)  
print('')
print(f'Você digitou {len(lista_numeros)} números. Os números digitados foram: {lista_numeros} ')
if '5' in lista_numeros:    
    print('O número 5 está na lista')
    
else:
    print('O número 5 não está na lista')
    
print('')
