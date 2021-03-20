import sys
import time

# l1 = [0,1,2,3,4]
# #l1 = 1234
# print(hasattr(l1, '__iter__'))

'''def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()
#print(g)
print(hasattr(g, '__iter__'))
print(g, '__next__')
print(next(g))
print(next(g))
print(next(g))'''

'''def gera():
    variavel = 'Valor1'
    yield variavel
    variavel = 'Valor2'
    yield variavel
    variavel = 'Valor3'
    yield variavel

g = gera()

for v in g:
    print(v)'''

#ex de consumo de memoria
l1 = [x for x in range(1000)]
print(type(l1))
#transformando em gerador
l2 = (x for x in range(1000))
print(type(l2))
print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
print(next(l2))
for v in l2:
    print(v)