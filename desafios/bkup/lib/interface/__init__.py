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


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[33m - \033[34m{item}\033[33m')
        contador += 1
    print(lista())
    opcao = leiaInt('\033[32mSua Opção: \033[33m')
    
