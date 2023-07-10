from interface import *
from arquivo import *
from time import sleep


arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)    
    

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    
    elif resposta == 2:
        cabecalho('Opção 2')

    elif resposta == 3:
        cabecalho('Saindo do sistema')
        break
    
    else:
        print('\033[31mDigite uma opção válida!\033[33m')
        sleep(2)
