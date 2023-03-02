altura = float(input('Qual a altura da parede? ->'))
largura = float(input('Qual a largura da parede? ->'))
area = altura*largura

print('Você vai precisar de {:.3} litros de tinta'.format(float(area/2)))
