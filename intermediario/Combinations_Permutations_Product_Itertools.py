'''
Combinations, Permutatons e Product - itertools
Combinação - Ondem não importa
Permutação - Ordem importa
ambos não repetem valores unicos
Produto - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product

pessoas = ['Marcos', 'Luciana', 'Camila', 'Mariana', 'Flora', 'Lorena']
'''
#dessa forma são combinados cada valor não repetindo os intes ex. Marcos e Luciana
#não vai se repetir Luciana e Marcos
for grupo in combinations(pessoas, 2):
    print(grupo)
'''
#dessa forma são combinados cada valor repetindo os intens ex. Marcos e Luciana
# e luciana e marcos
'''contador = 0
for grupo in permutations(pessoas, 2):
    print(grupo)
    contador += 1
print(contador)'''

#combina o valores repetindo ele mesmo ex. marcos e marcos
contador = 0
for grupo in product(pessoas, repeat=2):
    print(grupo)
    contador += 1
print(contador)
