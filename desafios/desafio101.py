def voto(ano):
    from datetime import date
    
    idade = date.today().year - ano
    
    if idade in [16,17] or idade > 70:
        return print(f'Com {idade} anos, o voto é opcional')
    
    elif idade >= 18:
        return print(f'Com {idade} anos, o voto é obrigatorio')
    
    else: 
        return print(f'Com {idade} anos, o voto é negado')
    
    
nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)
