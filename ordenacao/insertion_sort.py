"""
"Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. 
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort."
"""

import random
import time

lista_rand = random.sample(range(1, 860), 10)
print(lista_rand)
start = time.time()


# Funcao que realiza o insertion sort
def insertionSort(vetor):
    # A partir do primeiro elemento da lista
    for i in range(1, len(vetor)):

        pos = vetor[i]

        # move os elementos da lista, que sao menor que
        # o elemento chave para uma posicao a frente
        j = i-1
        while j >= 0 and pos > vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = pos


insertionSort(lista_rand)
print("\n lista ordenada: \n", lista_rand)
end = time.time()
print("\nTempo: ", end - start)
