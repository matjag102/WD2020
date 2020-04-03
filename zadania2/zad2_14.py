import math
liczba = float(input('podaj liczbę rzeczywistą >0: '))
try:
    wynik = math.sqrt(liczba)
    print('Pierwsiastek z liczby: ',str(liczba) + ' = ' + str(wynik))
except ValueError:
    print('liczba ujemna')
