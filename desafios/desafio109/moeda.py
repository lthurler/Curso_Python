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
