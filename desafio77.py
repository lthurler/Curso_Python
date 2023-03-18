tupla = ('gosto', 'fora', 'ruim', 'fome', 'banana')

for posicao in tupla:
    print(f'\nNa palavra {posicao.upper()} temos ', end ='')
    
    for letra in posicao:
        if letra in 'aeiou':
            print(letra, end =' ')

print('')
print('')
