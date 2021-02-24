""" 
Diversas maneiras diferentes de retirar itens duplicados de uma lista


os exemplos aqui demonstrados foram retirados do site:
https://www.peterbe.com/plog/fastest-way-to-uniquify-a-list-in-python-3.6
""" 



import time
import statistics
import random


# processos que preservam a ordem original
def f1(seq):
    lista = []
    for e in seq:
        if e not in lista:
            lista.append(e)
    return lista


def f2(seq):
    lista = []
    [lista.append(i) for i in seq if not lista.count(i)]
    return lista


def f3(seq, id_=None):
    if id_ is None:
        def id_(x): return x
    lista = {}
    resultado = []
    for item in seq:
        marcador = id_(item)
        if marcador in lista:
            continue
        lista[marcador] = 1
        resultado.append(item)
    return resultado


def f4(seq, id_=None):
    return list(_f4(seq, id_))


def _f4(seq, id_=None):
    lista = set()
    if id_ is None:
        for x in seq:
            if x in lista:
                continue
            lista.add(x)
            yield x

    else:
        for x in seq:
            x = id_(x)
            if x in lista:
                continue
            lista.add()
            yield x


def f5(seq, id_=None):
    return list(_f4(seq))


def f6(seq):
    return list(dict.fromkeys(seq))

# processos que nao preservam ordem original


def f11(seq):
    hash_ = {}
    [hash_.__setitem__(x, 1) for x in seq]
    return hash_.keys()


def f12(seq):
    return list(set(seq))


def f13(seq):
    return {}.fromkeys(seq).keys()


def f14(items):
    lista = set()
    for item in items:
        if item not in lista:
            lista.add(item)
    return list(lista)

# função geradora da lista desordenada


def lista_desordenada(length=50, amostra=30):
    """Função geradora de lista desordenada

    Args:
        length (int, optional): comprimento da lista. Defaults to 50.
        amostra (int, optional): intervalo das amostras. Defaults to 30.

    Returns:
        lista: retorna uma lista desordenada com comprimento = length e número de amostras=30
    """
    lista_rand = list(random.choice(range(amostra)) for i in range(length))
    return lista_rand




lista_rand = lista_desordenada()

print("Lista original")
print(lista_rand)

# sequencia das funções válidas
em_ordem = f1, f2, f3, f3, f4, f5, f6
fora_ordem = f11, f12, f13, f14


for i, f in enumerate(em_ordem):
    if i:
        funcao = em_ordem[i-1]
        out = funcao(lista_rand)
        print(out)

for i, f in enumerate(fora_ordem):
    if i:
        funcao = fora_ordem[i-1]
        out = funcao(lista_rand)
        print(set(out))
