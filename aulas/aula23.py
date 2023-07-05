try:
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))
    resultado = numerador / denominador

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'O resultado é {resultado:.1f}')

finally:
    print('Volte sempre!')
