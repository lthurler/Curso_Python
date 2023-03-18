mais1k = total = 0
mais_barato = preco_barato = ' ' 



while True:
    print('')
    nome = str(input('Digite o nome do produto > ')).strip()
    preco = float(input('Qual é o preço? > '))
    total += preco
    
    if preco_barato == ' ' or preco < preco_barato:
        preco_barato = preco    
        mais_barato = nome
        
    if preco > 1000:
        mais1k += 1
    
    continua = str(input('Deseja continuar (s/n) > ')).strip().lower()
    
    while continua != 's' and continua != 'n':
        print('Opção inválida! digite S para Sim e N para Não')
        continua = str(input('Deseja continuar (s/n) > ')).strip().lower()

    if continua == 'n':
        break

print('')
print(f'Foram gastos R${total:.2f} \n{mais1k} produtos custaram mais de R$1000.00 \nO mais barato foi {mais_barato} que custou R${preco_barato}')
print('')
