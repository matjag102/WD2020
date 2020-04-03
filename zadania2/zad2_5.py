a = int(input('Podaj  a: '))
b = int(input('Podaj  b: '))
c = int(input('Podaj  c: '))
if a > 0 and a <= 10:
    print('należy do (0,10>')
else:
    print('nie należy')
if a > b or b > c:
    print(' a>b lub b>c ')
else:
    print(' a<b lub b<c ')