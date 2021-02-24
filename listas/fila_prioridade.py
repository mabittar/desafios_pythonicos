"""
exemplo implementação de fila de prioridades
"""

import heapq


class DefineQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# Exemplo de uso


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


# criando a fila
q = DefineQueue()

# inserindo elementos na fila (elemento, prioridade)
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 3)
q.push(Item('vue'), 1)

# [(-5, 1, Item('bar')), (-1, 0, Item('foo')), (-3, 2, Item('spam')), (-1, 3, Item('vue'))]
print(q._queue)

# retirando elementos da fila em ordem de prioridade
print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be vue:", q.pop())
