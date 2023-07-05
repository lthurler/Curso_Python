segmento1 = float(input('Digite o valor do primeiro segmento: '))
segmento2 = float(input('Digite o valor do segundo segmento: '))
segmento3 = float(input('Digite o valor do terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    if segmento1 == segmento2 == segmento3:
        tipo = 'Equilátero'
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print('Esses segmentos podem formar um triângulo {} !'.format(tipo))
else:
    print('Esses segmentos não podem formar um triângulo!')
