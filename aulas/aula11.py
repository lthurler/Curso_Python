print('\033[7;33;45molá mundo!\033[m')
print('\033[1;33;45molá mundo!\033[m')
print('\033[1;33;42molá mundo!\033[m')
print('\033[0;33;42molá mundo!\033[m')
print('\033[0;31;44molá mundo!\033[m')
print('\033[0;31;40molá mundo!\033[m')
print('\033[7;40molá mundo!\033[m')

a = 3
b = 5

print('Os valores são \033[032m{}\033[m e \033[31m{}\33[m!!!'.format(a, b))

nome = 'Leandro'
print('Olá! {}{}{}!!!'.format('\033[1;31m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;40m'}

print('Ola! {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
