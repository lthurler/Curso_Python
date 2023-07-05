n1 = int(input('Digite um num: '))
n2 = int(input('Digite outro num: '))
soma = n1 + n2
multi = n1 * n2
div = n1 / n2
divInt = n1 // n2
pot = n1 ** n2

print('A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(
    soma, multi, div), end=' ')
print('Divisão inteira {} \n e a potência {}'.format(divInt, pot))
