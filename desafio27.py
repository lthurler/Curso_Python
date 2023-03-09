nome = str(input('Digite seu nome completo: ')).strip()
nome_split = nome.split()

print('Primeiro nome: {} \nÚltimo sobrenome: {}'.format(
    nome_split[0], nome_split[len(nome_split)-1]))
