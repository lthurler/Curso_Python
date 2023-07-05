numero = int(input('Digite um número inteiro qualquer: '))
opcao = int(input('''Qual a base de conversão?
                  
Digite ( 1 ) - para BINÁRIO
Digite ( 2 ) - para OCTAL
Digite ( 3 ) - para HEXADECIMAL

Qual é a opção?( 1 - 2 - 3 ): '''))

print(' ')
if opcao == 1:
    print('O número {} em binário é igual a {}'.format(
        numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} em octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} em hexadecimal é igual a {}'.format(
        numero, hex(numero)[2:]))
else:
    print('Opcão invalida! tente novamente')
print(' ')
