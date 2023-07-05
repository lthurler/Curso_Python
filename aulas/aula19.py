pessoas = {'nome': 'Leandro', 'sexo': 'M', 'idade': 46}

print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())

for chaves in pessoas.keys():
    print(chaves)

for chave, valor in pessoas.items():
    print(f'{chave} = {valor}')

del pessoas['sexo']
pessoas['nome'] = 'Gustavo'
pessoas['peso'] = 55.3

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

estado = {}
brasil = []

for cont in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)

for estado in brasil:
    print(estado)

for estado in brasil:
    for valor in estado.values():
        print(valor, end = ' ')
    print()   
