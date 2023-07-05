def metade(preco = 0.00, formato=False):
    resultado = preco/2
    return resultado if formato is False else moeda(resultado)


def dobro(preco = 0.00, formato=False):
    resultado = preco*2
    return resultado if formato is False else moeda(resultado)

def aumentar(preco = 0.00, porcentagem = 10, formato=False):
    resultado = preco + (preco * porcentagem/100)     
    return resultado if formato is False else moeda(resultado)


def diminuir(preco = 0.00, porcentagem = 10, formato=False):
    resultado = preco - (preco * porcentagem/100)
    return resultado if formato is False else moeda(resultado)


def moeda(preco = 0.00, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0.0,porcentagemA=10,porcentagemD=5):
    print('-' * 30)
    print('RESUMO DO PREÇO'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{porcentagemA}% de aumento: \t{aumentar(preco, porcentagemA, True)}')
    print(f'{porcentagemD}% de redução: \t{diminuir(preco,porcentagemD, True)}')
    print('-' * 30)
    