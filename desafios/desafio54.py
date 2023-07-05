from datetime import date

ano = date.today().year
conta_maior = 0
conta_menor = 0

for cont in range (1,8):
    nascimento = int(input('Digite o ano de nascimento da {} pessoa: '.format(cont)))
    if ano - nascimento >= 18:
        conta_maior += 1
    else:
        conta_menor += 1

print('Nos anos digitados {} tem maioridade e {} não tem maioridade.'.format(conta_maior, conta_menor))
