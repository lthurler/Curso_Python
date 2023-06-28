pessoa = {}
pessoas = []
mulheres = []
media_idade = 0
idade_acima = []
contador = 1

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = input('Sexo(M/F): ').upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    media_idade += pessoa['idade']
    
    if pessoa['sexo'] == 'M':
        mulheres.append(pessoa.copy())
        
    resposta = str(input("Deseja continuar? (s/n): "))
        
    print()
    
    while resposta not in 'sSnN':
        print()
        print('Resposta inválida! Digite somente (s/S) ou (n/N)')
        print()
        resposta = str(input("Deseja continuar? (s/n): "))
        print()
    
    if resposta in 'Nn':        
        break
    
    contador += 1

print()
print(f'Foram cadastradas {contador} pessoas')
media_idade = media_idade / contador
print(f'A media de idade do grupo é de {media_idade}')
print(f'mulheres cadastradas: {mulheres}')

if pessoas
    

4