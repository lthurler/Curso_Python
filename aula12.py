nome = str(input('Digite seu nome: ')).strip()

if nome == 'Leandro':
    print('nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome == 'João':
    print('seu nome é bem popular no BR!')
elif nome == 'Ana Claudia Jessica Juliana':
    print('belo nome feminino!')
else:
    print('nome normal!')

print('Tenha um bom dia {}'.format(nome))
