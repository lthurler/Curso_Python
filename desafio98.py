from time import sleep

def contador(inicio, fim , passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    sleep(2.5)    
    
    if inicio < fim : 
        contador = inicio
    
        while contador <= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador += passo
        print()
    
    else:
        contador = inicio
        
        while contador >= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador -= passo
        print()        
        

contador(1, 10, 1)
contador(10, 0, 2)
print()

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
