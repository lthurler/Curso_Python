distancia = int(input('Digite quantos km possui a sua viagem: '))

if distancia <= 200:
    print('O preço da sua passagem é de R$ {:.2f}'.format(distancia * 0.5))
else:
    print('O preço da sua passagem é de R$ {:.2f}'.format(distancia * 0.45))
