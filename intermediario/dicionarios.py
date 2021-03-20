#dicionario vc controla o indice
d1 = {'chave1':'valor da chave1'}

#add valor
d1['chave2'] = 'valor da chave2'
print(d1)
print(d1['chave2'])
for v in d1:
    print(v)

#outra forma de criar dicionário
d2 = dict(chave1='valor chave1', chave2='valor chave2')
print(d2)
print(d2['chave1'])

#outra forma de criar chave
d3 = {'chave1': 'valor chave1', 'chave 2': 'valor chave2'}
print(d3)

d3['chave3'] = 'valor chave 3'
print(d3)

#evitando excessção
d4 = {
    'str' : 'valor',
    123 : 'outro valor',
    (1,2,3,4) : 'Tupla',
}
#alterando valor da chave
d4['str'] = 'novo valor'
print()

#add dados com update
d4.update({'chave4' : 123})
print(d4)

if d4.get('str') is not None:
    print(d4.get('str'))

d4['novachave'] = 'nova chaved4'
if d4.get('novachave') is not None:
    print(d4.get('novachave'))
print()

#excluir chave:
del d4['str']
print(d4)

#checando se a chave existe (pode ser adicionado .keys() no final do codigo)
print('novachave' in d4)

#acessando valores da chave:
print(123 in d4.values())

#contar chaves
print(len(d4))
print()

#iterar chave
for d in d4:
    print('iterando nome da chave: ', d)
print()

#iterar valores das chaves
for d in d4.values():
    print('iterando valores das chaves: ', d)
print()

#vendo chave e valores
for chave_valores in d4.items():
    print(chave_valores)

print()
#acessado o indice do dicionário:
for chave_valores_indice in d4.items():
    print('oi', chave_valores_indice[0], chave_valores_indice[1])
print()
#desempacotar
for k, v in d1.items():
    print(k, v)

print()
#Dicionários dentro de dicionários e iterando dicionários filhos
clientes = {
    'cliente1' : {
        'nome' : 'Marcos',
        'sobrenome' : 'Santos',
    },
    'cliente2': {
        'nome': 'Luciana',
        'sobrenome': 'Farias',
    },
    'cliente3': {
        'nome': 'Camila',
        'sobrenome': 'Santos',
    },
    'cliente4': {
        'nome': 'Marianda',
        'sobrenome': 'Santos',
    },
}
'''print(clientes)
print()
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')'''

print()
# #copiando o dicionário raza:
# dicionario = {1 : 'a', 2 : 'b', 3 : 'c'}
# copia_dicionario = dicionario.copy()
# print(dicionario)
# print(copia_dicionario)
# print()
# copia_dicionario[1] = '-a'
# print(dicionario)
# print(copia_dicionario)

#forma correta de copiar dicionarios
import copy
d1 = {1: 'a', 2: 'b', 3: 'c', 'd':['José', 'Marcos']}
v = copy.deepcopy(d1)
v[1] = 'luiz'
v['d'][0] = 'Zé'
# print(d1)
# print(v)
#pode ser usado pop para elimina um item e popitem para eliminar o ultimo valor
d1.pop(1)
print(d1)
d1.popitem()
print(d1)
d2 = {5: 10, 6: 20}
#incluir um dicionario dentro de outro
d1.update(d2)
print(d1)