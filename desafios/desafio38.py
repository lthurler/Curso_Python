numero1 = int(input('Escreva um número para comparação: '))
numero2 = int(input('Escreva o outro número: '))

if numero1 > numero2:
    print('O número {} é o maior'.format(numero1))
elif numero2 > numero1:
    print('O número {} é o maior'.format(numero2))
else:
    print('Não existe valor maior, os dois são iguais')
