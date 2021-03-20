l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
l4 = []
l4.extend(l3)
l4.append(7)
letra = ['A', 'B', 'C', 'D', 'E', 'F','G']
maior = max(l4)
menor = min(l4)
i_maior = l4.index(maior)
i_menor = l4.index(menor)
letra_maior = letra[i_maior]
letra_menor = letra[i_menor]

print(letra_maior)
print(letra_menor)

print(l3)
print(l3[::-1])#inverte lista
print(l4)

for valor in l4:
    print(valor)

soma = 0
for valor in l4:
    soma += valor
print(soma)

l5 = [1, -25.9, True, 'banada']
for elem in l5:
    print(f'O tipo de l5 é {type(elem)} e seu valor é {elem}')
