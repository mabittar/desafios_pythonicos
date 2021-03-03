# How to Sort a Dictionary by Value in Python
import functools
import time
import random

# retorna o tempo de execução de uma função
def timer(func):
    @functools.wraps(func)
    def temporizador(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Terminou {} e {} secs".format(repr(func.__name__), round(run_time, 6)))
        return value

    return temporizador


@timer
def ordenacao1(dic):
	valores_ordenados = sorted(dic.values())
	dicionario_ordenado = {}

	for v in valores_ordenados:
		for k in dic.keys():
			if dic[k] == v:
				dicionario_ordenado[k] = dic[k]
				break
	# return dicionario_ordenado
	print("Ordenação1:", dicionario_ordenado)


@timer
def ordenacao2(dic):
	dicionario_ordenado = {}
	chaves_ordenadas = sorted(dic, key=dic.get)

	for k in chaves_ordenadas:
		dicionario_ordenado[k] = dic[k]
	# return dicionario_ordenado
	print("Ordenação2:", dicionario_ordenado)


import operator


@timer
def ordenacao3(dic):
	tupla_ordenada = sorted(dic.items(), key=operator.itemgetter(1)) # 1 for keys
	dicionario_ordenado = {k: v for k, v in tupla_ordenada}
	# return dicionario_ordenado
	print("Ordenação3:", dicionario_ordenado)


def gera_dict(n):
	mydict = {}
	for i in range(n):
		mydict['key'+str(i)] = random.randrange(10)
	return mydict

n = 45
dict_desordenado = gera_dict(n)

ordenacao1(dict_desordenado)
ordenacao2(dict_desordenado)
ordenacao3(dict_desordenado)