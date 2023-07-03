def notas(*nota, situacao = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.    
    """
    resposta = {}
    resposta['total'] = len(nota)
    resposta['maior'] = max(nota)
    resposta['menor'] = min(nota)
    resposta['média'] = sum(nota)/len(nota)
    
    if situacao:
        if resposta['média'] >= 7:
            resposta['situacao'] = 'BOA'
        
        elif resposta['média'] >= 5:
            resposta['situacao'] = 'RAZOAVEL'
        
        else:
            resposta['situacao'] = 'RUIM'
    
    return resposta

while True:
    totalNotas = int(input('Digite a(s) nota(s) do aluno: '))
    nota = []
    nota.append(totalNotas)

    continua = input('Deseja continuar? (S/N): ')
    print('')
    while not continua in 'SsNn':
        print('Dados inválidos! Por favor digite somente Ss para sim ou Nn para não')
    
    if continua in 'Nn':
        break

Mostrasituacao = input('Deseja mostrar a situação? (s/n) ')
situacao = False

while not Mostrasituacao in 'SsNn':
    print('Dados inválidos! Por favor digite somente Ss para sim ou Nn para não')
    
    if Mostrasituacao in 'Nn':
        situacao = False
        
    elif Mostrasituacao in 'Ss':
        situacao = True
        

notas(nota, situacao)
   