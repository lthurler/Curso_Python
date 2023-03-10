from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento

print(' ')
print('Quem nasceu no ano de {} tem {} anos em {}'.format(
    ano_nascimento, idade, ano_atual))
print(' ')

if idade < 18:
    print('Você ainda vai se alistar! Faltam {} ano(s) para o alistamento'.format(
        int(18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado! Já se passaram {} ano(s) desde a data do alistamento'.format(
        idade - 18))
else:
    print('Está na hora de se alistar!')

print(' ')
