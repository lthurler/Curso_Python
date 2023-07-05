from random import randint

conta_vitoria = 0

while True:
    print('')  
      
    par_impar = str(input('par ou impar? > ')).strip().lower()
    
    while par_impar != 'par' and par_impar != 'impar':
        print('Opção inválida!')
        par_impar = str(input('par ou impar? > ')).strip().lower()
    
    jogo_usuario = int(input('Qual é a sua jogada? (0-10) > '))
    
    while jogo_usuario not in range(0,10):
        print('Jogo inválido, só vale de 0 a 10 !')    
        jogo_usuario = int(input('Qual é a sua jogada? (0-10) > '))
    
    jogo_computador = randint(0,10)
    soma = jogo_computador + jogo_usuario    
    
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    
    print('')    
    print(f'Eu joguei {jogo_computador} e você {jogo_usuario}. Deu {soma} que é {resultado} !')
    print('')        
    
    if par_impar == 'par':
        
        if soma % 2 == 0:
            print('Ganhou!')
            conta_vitoria += 1
        else:
            print(f'Perdeu! Vc teve {conta_vitoria} vitórias consecutivas.')
            break
            
    else:
        
        if soma % 2 != 0:
            print('Ganhou!')
            conta_vitoria += 1
        else:
            print(f'Perdeu! Vc teve {conta_vitoria} vitórias consecutivas.')
            break        

    print('')
    print('Vamos jogar novamente')

print ('Fim de jogo')
print('')        
