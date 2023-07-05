dias = int(input("Qual foi a quantidade de dias? : "))
km = float(input("Qual foi a quantidade de km rodados? : "))
preco = 60 * dias + 0.15 * km

print('o valor a pagar é de R$ {:.2f}'.format(preco))
