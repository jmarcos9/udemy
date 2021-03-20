secreto = 'marcos'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Vocẽ Perdeu')
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Informe apenas letras!')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'Acertou!, a letra "{letra.upper()}" existe na palavra secreta')
    else:
        print(f'Errou!, a letra {letra} NÃO EXUSTE na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '#'
    if secreto_temporario == secreto:
        print(f'Você GANHOU!!! a Palavra era {secreto_temporario.upper()}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario.upper()}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()







