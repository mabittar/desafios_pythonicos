import random
import time

# gera lista aleatória
lista_rand = random.sample(range(1, 999), 100)


def maior(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        m = maior(lista[1:])
        return m if m > lista[0] else lista[0]


print(lista_rand)
start = time.time()
print("\n O maior número da lista é: {}".format(maior(lista_rand)))
end = time.time()
print("\n Tempo: {}.".format(end-start))
