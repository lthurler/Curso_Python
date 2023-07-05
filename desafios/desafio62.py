numero = int(input('Digite o número inicial da progressão aritimética: '))
razao = int(input('Digite a razão da progressão aritimética: '))
resultado = numero
contador = 1
termos = 0
adicionais = 10

while adicionais != 0:
    termos += adicionais
    
    while contador <= termos:
        print('{} -> '.format(resultado), end = '')    
        contador += 1
        resultado += razao
    print('Pausa')
    
    adicionais = int(input('Deseja termos? Quantos? '))
        
print('')
print('Progressão finalizada com {} termos'.format(termos))
print('')
