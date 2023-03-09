nome = str(input('Qual é o seu nome? ')).strip()

if nome == 'Leandro':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2

print('A sua média foi {:.2f}'.format(media))

if media >= 6.0:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')

print('PARABENS' if media >= 6 else 'ESTUDE MAIS!')
