numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolhido = int(input('Digite um número de 0 a 20 > '))

while escolhido not in range(0,21):
    print('Número inválido! escolha somente um número de 0 a 20')
    escolhido = int(input('Digite um número de 0 a 20 > '))

print('')
print(f'Você digitou o número {numeros[escolhido]}')
print('')
