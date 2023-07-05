preco = float(input('Digite o preço do produto R$ '))
condicao = int(input('''Qual é a opção da condição de pagamento?

( 1 ) à vista em dinheiro
( 2 ) à vista no cartão
( 3 ) em até 2x no cartão
( 4 ) 3x ou mais no cartão

( 1 - 2 - 3 - 4) ? '''))

print(' ')

if condicao == 1:
    print('O valor a ser pago será de R$ {:.2f} à vista'.format(
        preco - preco * 0.1))
elif condicao == 2:
    print('O valor a ser pago será de R$ {:.2f} à vista no cartão'.format(
        preco - preco * 0.05))
elif condicao == 3:
    print('O valor a ser pago será de R$ {:.2f} em até 2x no cartão'.format(
        preco))
elif condicao == 4:
    print('O valor a ser pago será de R$ {:.2f} em 3x ou mais no cartão'.format(
        preco * 0.2 + preco))
