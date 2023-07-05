teste = []
teste.append('Gustavo')
teste.append(40)

galera = []
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
# criando cópia pq se não vincula os arrays [:]
galera.append(teste[:])


print(galera)


# ---------------------------------------------------------------

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0] [0])


# ----------------------------------------------------------------

galera = list()
dado = list()
total_maior = total_menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor += 1
        
print(f'Temos {total_maior} maiores e {total_menor} menores de idade')