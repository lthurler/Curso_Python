def metade(preco = 0.00):
    resultado = preco/2
    return resultado


def dobro(preco = 0.00):
    resultado = preco*2
    return resultado


def aumentar(preco = 0.00, porcentagem = 10):
    resultado = preco + (preco * porcentagem/100)     
    return resultado


def diminuir(preco = 0.00, porcentagem = 10):
    resultado = preco - (preco * porcentagem/100)
    return resultado


def moeda(preco = 0.00, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
