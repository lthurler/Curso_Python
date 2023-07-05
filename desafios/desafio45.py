from random import randint

print('=' * 9)
print(' JOKENPÔ')
print('=' * 9)

opcao = int(input('''Qual é a sua opcão?

( 1 ) Pedra
( 2 ) Papel
( 3 ) Tesoura

( 1 - 2 - 3 ) ? > '''))
opcao_computador = randint(1, 3)

if opcao == 1:
    opcao = 'Pedra'
elif opcao == 2:
    opcao = 'Papel'
elif opcao == 3:
    opcao = 'Tesoura'
else:
    print('Opção inválida!! Tente novamente!')

if opcao_computador == 1:
    opcao_computador = 'Pedra'
elif opcao_computador == 2:
    opcao_computador = 'Papel'
else:
    opcao_computador = 'Tesoura'

print(' ')
print('-=' * 24)
print('   Você escolheu {} e o computador {} '.format(opcao, opcao_computador))
print('-=' * 24)
print(' ')

if opcao == opcao_computador:
    print('EMPATE!! Topa mais uma?')
elif (opcao == 'Pedra' and opcao_computador == 'Tesoura') or (opcao == 'Papel' and opcao_computador == 'Pedra') or (opcao == 'Tesoura' and opcao_computador == 'Papel'):
    print('Você GANHOU!!! Topa mais uma?')
else:
    print('Você PERDEU!! Topa mais uma?')
