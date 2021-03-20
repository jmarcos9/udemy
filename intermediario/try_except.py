try:
    a = 1/0
except NameError as erro:#Name usado quando a variavel não existe ex
    print('Erro do desenvolverdor')
except (IndexError, KeyError) as erro:#sado para lista e dicionario
    print('Erro de indice ou chave')
except Exception as erro:#erros diversos
    print('Ocorreu um erro inesperado')
else:#sempre é executado
    #print('Executado com sucesso')
    pass
finally:
    a = '' #usado tambem para finalizar conexões de baco... essa linha sempre será excutada