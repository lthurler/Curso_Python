lista_numeros = []

while True:
    numero = input('Digite um número: ')
    
    while not numero.isdigit():
        print('')
        print('Entrada inválida! Somente digite números')
        print('')
        numero = input('Digite um número: ')
    
    if numero not in lista_numeros:
        lista_numeros.append(numero)
        print('')
        print('Numero adicionado')
        print('')
    else:
        print('')
        print('Valor duplicado! Não adicionado a lista')
        print('')
    
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

lista_numeros.sort()
print(f'Você digitou os números: {lista_numeros}')
print('')
