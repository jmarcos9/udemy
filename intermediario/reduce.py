from dados_map import produtos, pessoas, lista
from functools import reduce

# #1 forma de acumar valores de uma lista (somar)
# acumula = 0
# for item in lista:
#     acumula += item
# print(acumula)

#acumulando com reduce
'''soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)
'''

#reduce dicionario
'''
soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print('Soma dos produtos é R${:.2f}'.format(soma_precos))
#media
print('Média dos produtos é R${:.2f}'.format(round(soma_precos / len(produtos))))
'''

#encontando a media de idad ecom reduce
soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade)
print('A media de idade é de {:.0f} anos'.format(soma_idade / len(pessoas)))
