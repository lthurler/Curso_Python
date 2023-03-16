media_idade = 0
contador_mulher = 0
homem_maior = 0
nome_velho = ''

for pessoa in range(1,5):
    print('')
    print('{}ª Pessoa'.format(pessoa))
    
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    sexo = str(input('Digite o sexo ( M/F ): ')).strip().lower()
    media_idade += idade
    
    if pessoa == 1 and sexo == 'm':
        homem_maior = idade
        nome_velho = nome
        
    if sexo == 'm' and idade > homem_maior:
        homem_maior = idade
        nome_velho = nome
        
    if sexo == 'f' and idade < 20:
        contador_mulher += 1
        
media_idade = media_idade / 4

print('')
print('A média de idade é {}'.format(media_idade))
print('O homem mais velho é o {} que possui {} anos'.format(nome_velho, homem_maior))
print('Existem {} mulheres com idade menor que 20 anos'.format(contador_mulher))
print('')
