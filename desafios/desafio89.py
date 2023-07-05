lista_alunos = []


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1) + (nota2) / 2
    lista_alunos.append([nome, [nota1, nota2], media])
    
    # while not nota1.isdigit:
    #     print('')
    #     print('Digito invalido! Por favor digite somente números!')
          
    continua = input('Deseja continuar? [S/N]: ')

    print('')

    while not continua in 'SsNn':
        print('Dados inválidos! Por favor digite somente Ss para sim ou Nn para não')

    if continua in 'Nn':
        break

print('')

print(f'{"Nº: ":<4} {"Nome: ":<10} {"média: ":>8}')
print('')

for index, aluno in enumerate(lista_alunos):
    print(f'{index:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')

while True:
    print("")
    opcao = int(input('Mostrar notas de qual aluno? ("Sair interrompe"): '))
    
    if opcao == 'sair':
        print('Fim')
        break
    
    if opcao <= len(lista_alunos):
        print(f'Notas de {lista_alunos[opcao][0]} {lista_alunos[opcao][1]}')
        