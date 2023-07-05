def area(largura, comprimento):
    area = largura * comprimento
    print()
    print (f'O terreno de largura {largura}m e comprimento {comprimento}m possui a área de {area}m²')


largura = None
comprimento = None

while largura is None:
    try:
        largura = float(input('Digite a largura do terreno: '))
    
    except ValueError:
        print("Entrada inválida. Digite somente valores numéricos.")

while comprimento is None:
    try:
        comprimento = float(input('Digite o comprimento do terreno: '))
    
    except ValueError:
        print("Entrada inválida. Digite somente valores numéricos.")    

area(largura, comprimento)
