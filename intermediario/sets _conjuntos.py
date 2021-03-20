# #s = set()
# s1 = {1, 2, 3, 4, 5}
# s1.add(6)
#remove elemento
# s1.discard(3)
# #s1.update('python')
# #s1.update([1,2,3,4,5])
# s2 = {5, 6, 7, 8, 9, 10}
# #s3 = s1 | s2 # | união
# #s3 = s1 & s2# interserção
# #s3 = s1 - s2 #diferença
# s3 = s1 ^ s2#estão nos dois sets mas não em ambos
#
# print(s3)

dic = {1,1,2,2,33,33,4,5,66,66,66,7,7,8,8,}
lista = list(dic)
lista.sort()
print(lista)

set_str = set()
set_str.update('marcos')
lista1 = list(set_str)
print(type(lista1))

for v in lista1:
    print(v)