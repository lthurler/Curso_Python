import random

print('')
print('Estou pensando em um número entre 0 e 10. Tente adivinhar!!')
print('')

tentativas = 1
numero = random.randint(0, 10)
chute = int(input('Qual é o seu chute? '))

while chute != numero:
    if chute > 10:
        print('NÚMEROS de 0 a 10! Tente novamente!')
        chute = int(input('Qual é o seu chute? '))
        tentativas += 1
        
    if numero > chute:       
        print('Errou! Mais..')
        tentativas += 1
    else:
        print('Errou! Menos..')
        tentativas += 1
        
    chute = int(input('Qual é o seu chute? '))

print('')
print('Acertou! Foram feitas {} tentativas ate o acerto'.format(tentativas))
print('')
