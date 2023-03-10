peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / altura ** 2

print(' ')
print('Seu IMC é igual a {:.1f}'.format(imc))
print(' ')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Seu peso é o ideal!')
elif 25 <= imc < 30:
    print('Você esta com sobrepeso!')
elif 30 <= imc < 40:
    print('Vecê está com obesidade!')
else:
    print('Você está com obesidade mórbida!!')

print(' ')
