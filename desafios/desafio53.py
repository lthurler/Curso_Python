frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[:: -1]

if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
