# pessoa = {
#     'nome': 'Marcos', 'idade': '40'
# }
# print(pessoa['idade'])
# #add elemento
# pessoa['sexo'] = 'M'
# print(pessoa)
# print()
# print(pessoa.values())
# print()
# print(pessoa.keys())
# print()
# print(pessoa.items())
# print()
# for k, v in pessoa.items():
#     print(f'{k}: {v}')
#
# locadora = []
# locadora.append(pessoa)
# print(locadora)
# filme = {
#      1: {'titulo': 'Star Wars',
#      'ano': 1977,
#      'diretor': 'George Lucas'
#     },
#     2: {'titulo': 'Avengers',
#      'ano': 2012,
#      'diretor': 'Joss Whedon'
#     },
#     3: {'titulo': 'Matriz',
#      'ano': 1999,
#      'diretor': 'Wachowski'
#     }
# }
#
# for k, v in filme.items():
#     print(k)
#     for k, v in v.items():
#         print(f'\t{k}: {v}')

pessoas ={'nome':'Marcos', 'sexo': 'M', 'idade': 40}
'''print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'{pessoas["nome"]}, sexo {pessoas["sexo"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
for k, v in pessoas.items():
    print(k, v)'''
# #apagando key e valor
# del pessoas['sexo']
# print(pessoas)
# print()

#alterando valor:
pessoas['nome'] = 'José Marcos'

# #add chave e valor:
# pessoas['peso'] = 79.45
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])
'''

estado = dict()
brasil = list()
for e in range(0,2):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #tem que fazer uma cópia para poder acessar os itens do dicionario em uma lista
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k} tem valor {v}')
print('#'*22)

for est in brasil:
    for v in est.values():
        print(v, end=" ")
    print()

