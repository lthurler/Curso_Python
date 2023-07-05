def maior (* numero):
    contador = maior = 0
    
    for valor in numero:
        if contador == 0:
            maior = valor
        
        else:
            if valor > maior:
                maior = valor
    
        contador += 1
    
    print(f'Foram informador {contador} valores ao todo')
    print(f'O maior valor informado foi {maior}')
    
maior(2, 9, 4, 5, 6, 1)
maior(4, 8, 0)
maior(1, 2)
maior(6)
maior()
