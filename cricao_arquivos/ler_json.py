import json

with open('arquivo_json.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)#convertendo para dicionario

for v, k in d1_json.items():
    print(v)
    for v in k.values():
        print(f'\t{v}')
