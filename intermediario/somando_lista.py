l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4,]

l_soma = []
#pegar o tamanho da lista e somar somente os indices corespondesntes em a e b
'''for i in range(len(l2)):
    l_soma.append(l1[i] + l2[i])
print(l_soma)'''
#forma 2
'''for i, _ in enumerate(l2):
    l_soma.append(l1[i] + l2[i])
print(l_soma)'''

#forma 3 list comprehension
l_soma = [x + y for x, y in zip(l1, l2)]
print(l_soma)


