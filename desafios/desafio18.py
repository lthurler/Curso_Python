from math import cos, sin, tan, radians

angulo = float(input("Digite o valor do angulo:"))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print("O angulo de {} graus, tem o cosseno de {:.2f} \no seno de {:.2f} \na tangente de {:.2f}".format(
    angulo, cosseno, seno, tangente))
