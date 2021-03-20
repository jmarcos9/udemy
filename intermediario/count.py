#count - itertools
from itertools import count
#contador = count(0, 2)
#contador = count(start=10, step=-2)
# print(next(contador))
# print(next(contador))
# for valor in contador:
#     print(round(valor,2))
#     if valor == 0:
#         break
contador = count()
prod = ['arroz','feijao','macarrao']
est = [100,200,300]
prod = zip(contador, prod, est)
print(list(prod))
