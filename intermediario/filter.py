from itertools import groupby
from dados_map import produtos, pessoas, lista
#retorna verdadeir ou falso usando lista filter
'''nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))
#list comprehension
lista2 = [x for x in lista if x > 5 and x < 9]
print(list(lista2))'''

#dicionario
'''l3 = filter(lambda p: p['preco'] > 100 and p['preco'] < 140, produtos)
for i in l3:
    print(i)
'''
#usando uma função com filter
'''def filtra(p):
    if p['preco'] > 120:
        return True

l4 = filter(filtra, produtos)
for i in l4:
    print(i)'''

#filter
'''
l5 = filter(lambda p: p['idade'] > 20, pessoas)
for i in l5:
    print(i)'''

def filtra_idade(idade):
    if idade['idade'] < 20:
        return True

l6 = filter(filtra_idade, pessoas)
for idade in l6:
    print(idade)

# ordena = lambda item: item['idade']
# pessoas.sort(key=ordena, reverse=True)
# pessoas_agrupados = groupby(pessoas, ordena)
#
# for agrupamento, valores_agupados in pessoas_agrupados:
#     print(f'Agrupamento Idade: {agrupamento}')
#     for idade in valores_agupados:
#          print(f'\t{idade}')
#     print()
