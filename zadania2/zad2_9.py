a = int(input('podaj liczbe:'))
suma = 0
while (a != 0):
    suma = suma + a % 10
    a = a // 10
print('suma=' + str(suma))

#http://www.algorytm.org/dla-poczatkujacych/suma-cyfr-liczby-calkowitej.html algorytm