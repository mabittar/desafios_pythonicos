from Lib.typing import List
import Lib.random
import time

#cria lista de amostra para ordenação
lista_rand = Lib.random.sample(range(1, 860), 100)
print(lista_rand)


def quick_sort(lista):
    """ 
        Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    if len(lista) < 2:
        return lista

    pivot = lista.pop()  # usando o último elemento como pivot
    maiores: List(int) = []  # para todos os elementos maiores que o pivot
    menores: List(int) = []  # para todos os elementos menores que o pivot

    for item in lista:
        (maiores if item > pivot else menores).append(item)

    return quick_sort(menores) + [pivot] + quick_sort(maiores)


if __name__ == '__main__':

    #entrada do usuário
    # user_input = input("Entre com a lista de números a ser ordenado separados por vírgula (,): ")
    # desordenada = [int(item) for item in user_input.split(",")]
    # print(quick_sort(desordenada))

    #entrada genérica
    start = time.time()
    print(quick_sort(lista_rand))
    end = time.time()
    print("\nTempo: ", end - start)
