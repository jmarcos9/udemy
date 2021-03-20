# l1 = [1,2,3,4,5]
# result = [v for v in l1 if v % 2 == 0]
#
# print(result)
# l1 = [
#     ('chave1', 'valor1'),
#     ('chave2', 'valor2')
# ]
# l1 = [
#     ('chave1',2),
#     ('chave2', 'valor2')
# ]
#d1 = dict(l1)
#d1 = {k: v*2 for k, v in l1}
#d1 = {k: v*2 for k, v in l1}
#d1 = {k.upper(): v.capitalize() for k, v in l1}
#d1 = {k: v for k, v in enumerate(range(5))}
#d1 = {k: v for k, v in enumerate(range(5))}
d1 = {f'chave_{x}': x**2 for x in range(1,5)}
print(d1)