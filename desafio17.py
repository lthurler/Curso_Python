from math import hypot

cateto_oposto = float(
    input("Digite o valor do cateto oposto do triângulo retângulo: "))
cateto_adjacente = float(
    input("Digite o valor do cateto adjacente do triângulo retângulo: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("O comprimento da hipotenusa, é {:.2f}".format(hipotenusa))
