def leiaInt(msg):
        
    while True:
        try:        
            numero = int(input(msg))
        
        except (ValueError, TypeError):
            print('\033[0;31mDigite um número inteiro válido\033[m')
            continue
        
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return numero


def leiaFloat(msg):
        
    while True:
        try:        
            numero = float(input(msg))
        
        except (ValueError, TypeError):
            print('\033[0;31mDigite um número real válido\033[m')
            continue
        
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return numero               


numero = leiaInt('Digite um número inteiro: ')
print(f'Você digitou {numero}')
