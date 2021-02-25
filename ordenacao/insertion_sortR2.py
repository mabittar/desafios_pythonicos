"""
"Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. 
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort."
"""

import random
import time

lista_rand = random.sample(range(1, 860), 10)
print(lista_rand)
start = time.time()


class InsertionSort(object):
    def __init__(self, list):
        self.list = list
        self.sorted = self.selection_sort()

    def __str__(self):
        return str(self.sorted)

    def selection_sort(self):
        for i in range(len(self.list)):
            valor_menor = 1
            for j in range(i + 1, len(self.list)):
                if self.list[j] < self.list[valor_menor]:
                    valor_menor = j
            self.list[i], self.list[valor_menor] = self.list[valor_menor], self.list[i]
        return self.list


if __name__ == '__main__':
    start = time.time()
    InsertionSort(lista_rand)
    print("\n lista ordenada: \n", lista_rand)
    end = time.time()
    print("\nTempo: ", end - start)
