from itertools import groupby, tee #tee faz copia do iterador
alunos = [
    {'nome': 'Marcos', 'nota': 10},
    {'nome': 'Luciana', 'nota': 8},
    {'nome': 'Camila', 'nota': 7},
    {'nome': 'Mariana', 'nota': 7},
    {'nome': 'Lorena', 'nota': 10},
    {'nome': 'Igor', 'nota': 8},
    {'nome': 'Flora', 'nota': 7},
]

#alunos.sort(key=lambda item: item['nota'], reverse=True)
# for aluno in alunos:
#     print(aluno)

#sunstitui o for anterior
ordena = lambda item: item['nota']
alunos.sort(key=ordena, reverse=True)
alunos_agrupados = groupby(alunos, ordena)

# for agrupamento, valores_agupados in alunos_agrupados:
#     print(f'Agrupamento Nota: {agrupamento}')
#     for aluno in valores_agupados:
#         print(f'\t{aluno}')
#     print()

for agrupamento, valores_agrupados in alunos_agrupados:
    v1, v2 = tee(valores_agrupados) # faz copia dos valores para N variave

    print(f'Agrupamento {agrupamento}')

    for aluno in v1:
        print(f'\t{aluno}')

    qtde = len(list(v2))#como o len é um iterador apos passar por ele zera os valores e proximos fors não funcionarão
    print(f'\t \t{qtde} alunos tiraram a nota {agrupamento}')

