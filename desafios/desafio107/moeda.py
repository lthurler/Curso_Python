def metade(preco):
    resultado = preco/2
    return resultado


def dobro(preco):
    resultado = preco*2
    return resultado


def aumentar(preco,porcentagem = 10):
    resultado = preco + (preco * porcentagem/100)     
    return resultado


def diminuir(preco, porcentagem = 10):
    resultado = preco - (preco * porcentagem/100)
    return resultado
