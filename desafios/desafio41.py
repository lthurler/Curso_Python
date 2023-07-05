from datetime import date

data_atual = date.today().year
data_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = data_atual - data_nascimento

print(' ')
print('Você tem {} anos'.format(idade))
print(' ')

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')

print(' ')
