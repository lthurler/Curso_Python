sexo = str(input('Digite seu sexo (m/f): ')).strip().lower()[0]

while sexo not in 'mf':
    sexo = str(input('Sexo não corresponde, Digite novamente seu sexo (m/f): ')).strip().lower()[0] 

print('')
print('Sexo {} registrado com sucesso'.format(sexo))
print('')
