valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do seu salário? '))
anos = float(input('Em quantos anos você pretende pagar? '))
prestacao = valor_casa / (anos*12)

if prestacao <= salario * 0.3:
    print('Seu crédito foi aprovado! \nO valor de cada prestacão é de R${:.2f} durante {} anos'.format(
        prestacao, anos))
else:
    print('Seu crédito não foi aprovado!')
