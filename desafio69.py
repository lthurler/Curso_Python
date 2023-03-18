homens = 0
anos18 = 0
mulheres20 = 0

while True:
    print('')
    idade = int(input('Digite sua idade > '))
    
    while idade <= 0:
        print('idade invalida! Digite novamente')
        idade = int(input('Digite sua idade > '))
        
    sexo = str(input('Digite seu sexo (M/F) > ')).strip().lower()
    
    while sexo != 'm' and sexo != 'f':
        print('Sexo inválido! Digite somente M para Masculino e F para Feminino!')
        sexo = str(input('Digite seu sexo (M/F) > ')).strip().lower()
    
    if sexo == 'm':
        homens += 1  
    
    if idade > 18:
        anos18 += 1
    
    if sexo == 'f' and idade < 20:
        mulheres20 += 1
        
    print('')
    continua = str(input('Deseja continuar (S/N)? > ')).strip().lower()
    
    while continua != 's' and continua != 'n':
        print('Opção inválida! digite somente S para sim ou N para não')
    
    if continua == 'n':
        break

print('')
print(f'Foram cadastradas {anos18} pessoas com mais de 18 anos \nForam cadastrados {homens} homens \nForam cadastradas {mulheres20} mulheres com menos de 20 anos.')
print('')   
    