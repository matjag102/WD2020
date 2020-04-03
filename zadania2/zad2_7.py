lista = []
for i in range(1, 5, 1):
    a = input('podaj '+' liczbe: ')
    lista.append(int(a))
for i in range(0, 4, 1):
    print(str(lista[i]) + '^2 = ' + str(lista[i] ** 2))