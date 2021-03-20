'''x =  0
while x < 5:
    print(x)
    x += 1

x = 0
while x <= 5:
    if x == 3:
        x += 1
        continue
    print(x)
    x += 1'''

x = 0
'''while x <=5:
    y = 0
    while y <= 5:
        print(f'({x},{y})')
        y += 1
    x += 1
print('Acabou')'''


while True:
    n1 = (input('Número 1: '))
    if not n1.isnumeric():
        print('Digite números!')
        continue

    n2 = input('Número 2: ')
    if not n2.isnumeric():
        print('Digite números!')
        continue

    op = input('Operador: ')

    n1 = int(n1)
    n2 = int(n2)

    if op == '+':
        total = n1 + n2
    elif op == '-':
        total = (n1 - n2)
    elif op == '*':
        total = n1 * n2
    elif op == '/':
        total = n1 / n2
    print(f'{n1} {op} {n2} = {total}')



