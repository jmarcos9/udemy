def func(arg1, arg2):
    return arg1 * arg2
var = func(3,3)
print(var)

#anonimas
a = lambda x, y: x * y
print(a(3,3))

l = [
    ['p1', 1500],
    ['p2', 2500],
    ['p3', 500],
    ['p4', 5500],
    ['p5', 100],
]
# #usando .sort é alterado a lista - deve criar uma função para poder ordenar
# def alternar_sort(item):
#     #ordena pelo indice 1 da lista dentro da lista
#     return item[1]
# l.sort(key=alternar_sort, reverse=True)
# print(l)

# #fazendo a ordenação com a expressão lambda, lembrando que o sort altera a lista (valores x indice
# l.sort(key=lambda item: item[1])
# print(l)

#ordenando alista sem alterar a mesma função sorted com uso da expressão lambda
#ordenando pelo valor
print(sorted(l, key=lambda i: i[1], reverse=False))
#ordendando pelo produto
print(sorted(l, key=lambda i: i[0], reverse=True))
print(l)


var = lambda x, y: x + y
print(var(5, 5))

def soma(x, y):
    return x + y
print(soma(5, 5))
