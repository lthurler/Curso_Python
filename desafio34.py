salario = float(input('Qual o valor do salário? R$'))

if salario > 1250:
    print('O salário com aumento é de R${:.2f}'.format(
        salario * 0.1 + salario))
else:
    print('O salário com aumento é de R${:.2f}'.format(
        salario * 0.15 + salario))
