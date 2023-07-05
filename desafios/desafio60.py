# from math import factorial

numero = int(input('Digite um número: '))
# fatorial = factorial(n)
fatorial = 1
contador = 1

# for count in range (2,numero + 1):
#   fatorial *= count

while contador < numero:
    contador += 1
    fatorial *= contador

print('O fatorial de {} é igual a {}'.format(numero, fatorial))
