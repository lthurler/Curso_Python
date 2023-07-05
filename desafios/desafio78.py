lista_numeros = list()
posicao_maior = list()
posicao_menor = list()
maior = menor = 0
 
for cont in range(0, 6):
    lista_numeros.append(int(input('Digite um número: ')))

    if cont == 0:
        maior = menor = lista_numeros[cont]        
    
    if lista_numeros[cont] > maior:
        maior = lista_numeros[cont]
            
    if lista_numeros[cont] < menor:
        menor = lista_numeros[cont]
        
for index, valor in enumerate(lista_numeros):
    if valor == maior:
        posicao_maior.append(index)
    
    if valor == menor:
        posicao_menor.append(index)

print('')
print(f'Você digitou os valores {lista_numeros}')
print('')
print(f'O maior valor foi {maior} na posição {posicao_maior}')
print(f'O menor valor foi {menor} na posição {posicao_menor}')
print('')
 