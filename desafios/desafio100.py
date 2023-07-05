from random import randint

sorteados = []

def sorteia():    
    for cont in range (1,6):
        numero = randint(0,100)
        sorteados.append(numero)
    
    print()
    print(f'Os números sorteados foram {sorteados}')


def somaPar(sorteados):
    soma_par = 0
    
    for cont, valor in enumerate(sorteados):
        if valor %2 == 0:
            soma_par += valor
    
    print(f'A soma dos números pares sorteados é de {soma_par}')
    print()
    

sorteia()
somaPar(sorteados)     
        