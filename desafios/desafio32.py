from datetime import date

ano = int(input(
    'Digite um ano para ver se é bissexto. Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))
