'''def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('log',error)#log do tratamento pode ser salvo em aruivo de log erro
        raise#relançar a cxcerção para outro try

#esse try não vai funcionar mais... tem que incluir o raise no primeiro tratamento para este segundo funcionar
try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)'''

# lançando sua propria exceção
def divide(n1, n2):
    if n2 == 0 or n1 == 0:
        raise ValueError('N1 ou N2 não pode ser 0')
    return n1 / n2
try:
    print(divide(0, 2))
except ValueError as error:
    print(error)
