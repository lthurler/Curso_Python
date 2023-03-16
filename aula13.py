for c in range(0, 6):
    print('oi')
print('FIM')

for c in range(1, 7):
    print(c)
print('fim') 

for c in range(6, 0, -1):
    print(c)
print('fim') 

for c in range(0, 7, 2):
    print(c)
print('fim')

n = int(input('Digite um número: '))

for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('Fim')

soma = 0
 
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    soma += n
print('O somatorio de todos os valores foi: {}'.format(soma))
