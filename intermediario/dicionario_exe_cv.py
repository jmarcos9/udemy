situacao = dict()
for aluno in range(0,1):
    situacao['nome'] = str(input('Digite o Nome: '))
    situacao['media'] = float(input(f'Informe a média de {situacao["nome"]}: '))
    if situacao['media'] >= 7:
        if situacao['media'] > 10 and situacao['media'] < 0:
            print('Erro na digitação')
            break
        situacao['situacao'] = 'Aprovado'
    elif situacao['media'] >= 4:
        situacao['situacao'] = 'Recuperação'
    elif situacao['media'] < 0:
        print('Erro na digitação')
        situacao['situacao'] = 'Reprovado'
    else:
        print('Reprovador')

for k, v in situacao.items():
    print(f'{k} é igual a {v}')
