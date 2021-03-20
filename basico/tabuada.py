c = 0
while True:
    n = int(input('Tabuada de qual valor? '))
    print('#' * 11)
    for t in range(1,11):
        t *= n
        c += 1
        print(f'{n} x {c} = {t}')
    print('#' * 11)
    break
