import time
import random

# remove elementos da lista usando o return
def remove_duplicados(items):
    lista = set()
    lista_aux = lista.add
    return [item for item in items if not (item in lista or lista_aux(item))]


# remove elementos da lista usando yield
def remove_duplicados_y(items):
    lista = set()
    for item in items:
        if item not in lista:
            yield item
            lista.add(item)


if __name__ == '__main__':

    # gerando lista aleatória
    lista_rand = list(random.choice(range(30)) for i in range(50))
    print("Lista original")
    print(lista_rand)

    print("Usando Yeild")
    # inicio do cronometro
    start_yield = time.time()
    print(list(remove_duplicados_y(lista_rand)))
    # fim do cronometro
    end_yield = time.time()
    print("Tempo para remover duplicados e manter a ordem original: ",
          (end_yield - start_yield))

    start_return = time.time()
    print("Usando return")
    print(list(remove_duplicados(lista_rand)))
    end_return = time.time()
    print("Tempo para remover duplicados e manter a ordem original: ",
          (end_return - start_return))
