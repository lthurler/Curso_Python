cont = 1

while True:
    print(cont, ' ', end = '')
    cont += 1

print('Acabou')

# --------------------------
n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

print('A soma vale {}'.format(s))

# --------------------------
n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

print(f'A soma vale {s}')

# ---------------------------
nome ='José'
idade = 33
salario = 987.35

print(f'O {nome:-^20} tem {idade: ->20} anos e ganha R${salario:.2f}.')
