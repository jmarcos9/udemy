#Zip - unindo iteraveis - aNÃO PRECISA IMPORTAR MODULO
#zip_longest - intertools
from itertools import zip_longest, count #importar modulo
indice = count()
cidades = ['são paulo', 'belo horizonte', 'salvador', 'recife', 'monte belo', 'olinda']
estados = ['SP', 'MG', 'BA', 'PE']


'''cidades_estados = zip(cidades, estados) # pode inverter pa amudar a ordem estados, cidades
não é a melhor forma de trabalhar
print(next(cidades_estados))
print(next(cidades_estados))
pode ser convertido em lista
print(list(cidades_estados))
pode ser convertido em dict
print(dict(cidades_estados))

for valor in cidades_estados:
    #print(valor[0], valor[1])
    print(valor)'''
#fillvalue insere valor padrao definido pelo programador
'''cidades_estados = zip_longest(# pode inverter pa amudar a ordem estados, cidades
    cidades,
    estados,
    fillvalue='Estado N/A'
)
#print(list(cidades_estados))
for v in cidades_estados:
     print(f'Cidade: {v[0]}, Estado: {v[1]}')
     '''
cidades_estados = zip(# pode inverter pa amudar a ordem estados, cidades
    indice,
    cidades,
    estados,
)
for indice, cidades, estados in cidades_estados:
      print(indice, cidades, estados)
# for valor in cidades_estados:
#     print(valor)

