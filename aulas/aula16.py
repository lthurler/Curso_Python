lanche = ('Hambúrguer','Suco','Pizza', 'Pudim', 'Batata frita')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[0:3])
print(lanche[:2])
print(lanche[-3:])

# --------------------------
for comida in lanche:
    print(f'Eu vou comer {comida}')
    
# --------------------------
print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'{cont} ', end ='')
    print(f'{lanche[cont]} ', end ='')

# --------------------------
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') 

# ---------------------------
print (sorted(lanche))

# ---------------------------
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(c.count(5))
print(c.index(8))
print(c.index(4))
print(c.index(2))
print(c.index(2, 4))
print(c.index(5))
print(c.index(5, 1))

# ---------------------------
pessoa = ('Gustavo', 39, 'M', 99.88)

print(pessoa)

# tuplas são imutáveis, somente aceitando del dela toda
