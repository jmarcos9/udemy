import os
import json
'''file = open('abcde.txt', 'w+')#w+ ler e escrever
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0, 0)#manipula o cursor do aquivo
print(file.read())
file.seek(0, 0)
print('#'*10)

print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#'*10)

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')
file.close()'''
'''try:
    file = open('file.txt', 'w+')
    file.write('linha\n')
    file.write('José Marcos')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
'''
# forma correta
#with é gerenciador de arquivo fecha o arquivo sem pecisar uar o close
# with open('arquivo.txt', 'w+') as file:
#     file.write('José\n')
#     file.write('Marcos\n')
#     file.write('dos Santosa\n')
#     file.seek(0, 0)
#     print(file.read())
# print('#'*30)
# #leitura
# with open('arquivo.txt', 'r') as file:
#     print(file.read())
print('#'*30)
#ativa o append mode.. e coloca o cursor no final
'''with open('arquivo.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0, 0)
    print(file.read())'''

#criar arquivo json
d1 = {
    'Pessoa1':{
        'nome':'Marcos',
        'idade': 40,
    },
    'Pessoa2':{
        'nome':'Luciana',
        'idade': 39,
    }
}
d1_json = json.dumps(d1, indent=True)
with open('arquivo_json.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)

#deleta o arquivo
#os.remove('arquivo.txt')