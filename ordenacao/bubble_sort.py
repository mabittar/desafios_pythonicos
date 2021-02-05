import random
import time


# gera lista aleatória
lista_rand = random.sample(range(1, 860), 100)
print(lista_rand)


# bubble_selection
def bubble(lista):
    """
    Função de ordenação do tipo bubble sorte
    input: Recebe uma lista de números desordenada
    output: retorna a lista inicial ordenada

    """
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca os elementos de posição
                lista[i], lista[i+1] = lista[i+1], lista[i]


# inicia o contador de tempo
start = time.time()
# chama a função de ordenação
print(bubble(lista_rand))
# encerra o cronometro
end = time.time()
print("\n Tempo: ", end-start)
