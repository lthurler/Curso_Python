aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
    
elif aluno['media'] >= 5 < 7:
    aluno['situacao'] = 'Recuperação'
    
else:
    aluno['situacao'] = 'Reprovado'

print()
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')
print()
