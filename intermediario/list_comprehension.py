
l1 = [1, 2, 3, 4, 5,]
ex1 = [v for v in l1]
#print(ex1)
ex2 = [v * 2 for v in l1]
#print(ex2)
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
#print(ex3)

l2 = ['luiz', 'mauro', 'maria']
ex4 = [var.replace('a', '@').upper() for var in l2]
#print(ex4)

tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)
#ex5 = [(x, y) for x, y in tupla]
#invertendo chave x valo:
ex5 = [(y, x) for x, y in tupla]
#print(ex5)
ex5 = dict(ex5)
print(ex5['valor2'])

l3 = list(range(10))
#ex6 = [v for v in l3 if v % 2 == 0 if v % 3 == 0 if v % 8 == 0]
#print(ex6)
ex7 = [v if v % 2 == 0 and v % 8 == 0 else '' for v in l3]
#print(ex7)

exe8 = '0123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
#tupla
#solucao = [exe8 (i, i + n) for i in range(0, len(exe8), n)]
#lista
solucao = [exe8[i: i + n] for i in range(0, len(exe8), n)]
solucao = '.'.join(solucao)
print(solucao)

