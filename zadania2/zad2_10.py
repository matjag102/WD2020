a = int(input('podaj wielkość wieży<10: ''\n'))
if a >10:
    print('zla wartosc')
else:
    for i in range(0, a, 1):
        for j in range(0, i + 1, 1):
            print('A', end='')
        print()