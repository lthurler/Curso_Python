lista_numeros = list()
maior = 0
menor = 0

for index in range(0, 6):
    lista_numeros.append(int(input('Digite um número: ')))

    if index == 0:
        maior = menor = lista_numeros[index]
    
    if lista_numeros[index] > maior:
        maior = lista_numeros[index]
    
    if lista_numeros[index] < menor:
        menor = lista_numeros[index]
    