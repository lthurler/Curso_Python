velocidade = float(input('Qual a velocidade do seu carro nesse momento? '))

if velocidade > 80:
    print('Você foi multado! \nO valor da sua multa é R${:.2f}'.format(
        (velocidade - 80)*7))
else:
    print('Tá tranquilo!')
