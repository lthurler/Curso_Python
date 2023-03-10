nota1 = float(input('Digite o valor da sua primeira nota: '))
nota2 = float(input('Digite o valor da sua segunda nota: '))
media = (nota1 + nota2) / 2

print(' ')
print('Sua média foi {}'.format(media))
print(' ')

if media < 5:
    print('Você foi reprovado!')
elif media >= 5 and media <= 6.9:
    print('Você está em recuperação!')
else:
    print('Você está aprovado!')

print(' ')
