nome = str(input('Qual é seu nome completo? ')).strip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))

primeiro_nome = nome.split()
print('Seu primeiro nome possui {}'.format(len(primeiro_nome[0])))
