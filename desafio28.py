import random

print('Estou pensando em um número entre 0 e 5. Tente adivinhar!!')

num = random.randint(0, 5)
chute = int(input('Qual é o seu chute? '))

if chute == num:
    print('Acertou! Cagão do #$%¨%! ')
else:
    print('Não é :P ! o número era {}'.format(num))
