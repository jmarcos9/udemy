from dados_map import produtos, pessoas, lista
'''
usado em listas e dicionarios
'''


#map retorna o obj.. tem que fazer o cast para lita
'''
#nova_lista = map(lambda x: x * 2, lista)
#list compreshension
nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))'''

'''#dicionario
#add 5% em cada preço
# precos = map(lambda p: p['preco'], produtos)
# for preco in precos:
#     print(preco, end=' ')
ajuste = 1.5
def ajuste_preco(p_ajustado):
    p_ajustado['preco'] = round(p_ajustado['preco'] * ajuste) #ou 1.5 no lugar do ajuste
    return p_ajustado

produtos_precos_ajustados_5 = map(ajuste_preco, produtos)
for produto in produtos_precos_ajustados_5:
    print(produto)
'''
ajuste = 1.5
def ajuste_preco(p_ajustado):
    p_ajustado['novo_preco'] = round(p_ajustado['preco'] * ajuste) #ou 1.5 no lugar do ajuste
    return p_ajustado

novo_preco = map(ajuste_preco, produtos)
for p_novo in novo_preco:
    print(p_novo)

print()

#dicionario com strings
#list comprehensions não consegui rodar
#nomes = [x for x in pessoas['nome']]
#print(nomes)
#map
'''nomes = map(lambda p, i: p['nome'], pessoas)
for nome in nomes:
    print(nome)'''

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)