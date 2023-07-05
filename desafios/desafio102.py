def fatorial(numero, show = False):
    fatorial = 1
    for cont in range(numero, 0 , -1):
        if show:
            print(cont, end='')
            
            if cont > 1:
                print(f' x ', end='')
                
            else:
                print(' = ', end='')
                
        fatorial *= cont
    return fatorial


numero = int(input('Digite um número para mostrar o seu fatorial: '))
show = input('Deseja mostrar o fatorial?(s/n) ')

if show in 'Ss':
    show = True
    
else:
    show = False

fatorial(numero, show)
