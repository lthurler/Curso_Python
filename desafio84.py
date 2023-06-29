dados = list()
pessoas = list()
mais_pesados = list()
mais_leves = list()
maior = menor = 0

while True:
    print('')
    dados.append(input('Nome: '))
    dados.append(input('peso: '))
        
    
    while not dados[1].isdigit():        
        print('Dados inválidos! Por favor digite somente números')
        dados[1] = (input('peso: '))
            
    if len(pessoas) == 0:
        maior = menor = dados[1]
    
    else:
        if int(dados[1]) > int(maior):
            maior = dados[1]
        
        if int(dados[1]) < int(menor):
            menor = dados[1]
    
    pessoas.append(dados[:])
    dados.clear()   
    
    continua = input('Deseja continuar? (S/N): ')
    print('')
    while not continua in 'SsNn':
        print('Dados inválidos! Por favor digite somente Ss para sim ou Nn para não')
    
    if continua in 'Nn':
        break
    

print('')
print(f'As pessoas são {pessoas} pessoas')
print(f'Ao todo foram cadastradas {len(pessoas)}')
print(f'O maior peso foi o de {maior} kg')
print(f'O menor peso foi o de {menor} Kg')    

for p in pessoas:
    if p[1] == maior:
        print(f'A pessoa mais pesada é {p[0]}')
    if p[1] == menor:
        print(f'A pessoa mais leve é {p[0]}')
        