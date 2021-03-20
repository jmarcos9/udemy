texto = 'python'
for i in texto:
     print(i)
tam = len(texto)

for i in range(10, -2, -2):
    print(i)
print('##########')
for i in range(12):
    if i % 2 == 0:
        print(i)

nova_string = ''
for letra in texto:
    if letra == 'p':
        nova_string += letra.upper()
    elif letra == 't':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)
