# from desafio115.lib.interface import *


from desafios.desafio115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    
    except FileNotFoundError:
        return False
    
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    
    except:
        print('Houve um erro na criação do arquivo!')
    
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    
    except:
        print('Erro ao ler o arquivo!')
        
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in arq:
            dados = linha.split(';')
            dados[1] = dados[1].replace('/n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')        
    
    finally:
        arq.close()
        


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
        
    except:
        print('Houve um erro na abertura do arquivo')
    
    else:
        try:
            arq.write(f'{nome};{idade}/n')
        
        except:
            print('Houve um erro na hora de escrever os dados')
        
        else:
            print(f'Novo registro de {nome} adicionado')
            arq.close()
            