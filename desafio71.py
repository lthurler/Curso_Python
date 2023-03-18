print('')
valor = int(input('Qual o valor que será sacado? > '))
print('')
cedula = 50
total_cedula = 0

while True:
    if valor >= cedula:
        valor -= cedula
        total_cedula += 1
        
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        
        if cedula == 50:
            cedula = 20
            
        elif cedula == 20:
            cedula = 10
            
        elif cedula == 10:
            cedula = 1
        
        total_cedula = 0
        
        if valor == 0:
            break
        
print('')