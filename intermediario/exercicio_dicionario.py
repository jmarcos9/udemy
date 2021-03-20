#Sistema de perguntas e respostas com dicionários em Python
perguntas = {
    'pergunta 1': {
        'pergunta': 'Qunato é 2+2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
    'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Qunato é 3x2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '6',
        },
    'resposta_certa': 'c',
    },
}

print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas:')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Resposta Alternativa: ')

    if resposta_user == pv['resposta_certa']:
        print('Acertou!')
        respostas_certas += 1
    else:
        print('NÂO acertou!')

    print()
