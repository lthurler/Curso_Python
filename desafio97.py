def mensagem(msg):
    tamanho = len(msg) +4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


msg = input('Escreva uma mensagem: ')

mensagem(msg)
