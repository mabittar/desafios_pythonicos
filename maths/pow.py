def potencia(x, y):
    if y == 0:
        return 1

    if y >= 1:
        return x * potencia(x, y - 1)


print(potencia(4, 4))
