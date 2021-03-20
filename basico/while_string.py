frase =  'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
nova_frase = ''
cont = 0
# while cont < tamanho_frase:
#     # print(cont, frase[cont])
#     nova_frase += frase[cont]
#     print(nova_frase)
#     cont += 1
# print(nova_frase)

while cont < tamanho_frase:
    letra = frase[cont]
    if letra == 'r':
        nova_frase += 'R'
    else:
        nova_frase += letra
    cont += 1
print(nova_frase)