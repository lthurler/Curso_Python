from time import sleep

print('')

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
resultado = 0
operacao =0

while operacao != 5:
    print('')
    print('Opções: [1 a 5]:')
    print('')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')
    print('')

    operacao = int(input('Qual operação deseja fazer com os números? '))

    print('')
    
    if operacao == 1:
        resultado = numero1 + numero2
        print('A soma de {} + {} é {}'.format(numero1,numero2,resultado))
        
    elif operacao == 2:
        resultado = numero1 * numero2
        print('A multiplicação de {} * {} é {}'.format(numero1,numero2,resultado))
        
    elif operacao == 3:
        if numero1 > numero2:
            resultado = numero1
        else:
            resultado = numero2
        print('Entre {} e {} o maior é {}'.format(numero1,numero2,resultado))
        
    elif operacao == 4:
        print('Informe os números novamente:')
        print('')
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
    
    elif operacao == 5:
        print('Fim!')
        
    else:
        operacao = int(input('Operação inválida! Digite um número de 1 a 5: '))
    
    sleep(3)
    