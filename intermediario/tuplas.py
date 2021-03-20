t1 = (1,2,3,'a', 'marcos')
print(t1[4])

for v in t1:
    print(v)
print(t1[2:])

t2 = 1, 2, 3,'a', 'marcos'
print(t2)
#para criar uma tupla com um único elemento sem parentese devo colocar a virgura após o elemento
t3 = 1,
print(type(t3))

#concatener tuplas
t4 = t1 + t2 + t3
print(t4)

#desempacotando a tupla
*_, n1, n2  = t4
print(n1, n2)

#repetir a tupla
t_repetir = (5,4,3,2,1) * 2
print(t_repetir)

#converter tupla em lista (modificar) e depois converter a lista em tupla
t_modificar = (1,2,3,4)
t_modificar = list(t_modificar)
t_modificar[2] = 3000
print(t_modificar)
t_modificar = tuple(t_modificar)
print(t_modificar)