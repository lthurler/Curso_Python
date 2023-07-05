contador = 0
soma = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))
    
    if numero == 999:
        break
    
    soma += numero
    contador += 1
    
    
print(f'Foram digitados {contador} números e a soma deles é igual a {soma}.')
