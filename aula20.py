def soma(a, b):
    resultado = a + b
    print(resultado)
    
    
soma(6,4)

def contador (*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e ao todo {tamanho} números.')

    
contador(2, 1, 7)
contador(8, 0)
contador(2, 3, 4, 5, 6)

def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 1, 2]
dobra(valores)
print(valores)
