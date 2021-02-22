def bubble_sort_v2(lista):
    length = len(lista)
    for i in range(length - 1):
        troca = False
        for j in range(length - 1 - i):
            if lista[j] > lista[j + 1]:
                troca = True
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if not troca:
            break  # Para a iteração se a lista estiver ordenada
    return lista


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input(
        "Entre com a lista de números a ser ordenado, separados por ,: ").strip()
    desordenada = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubble_sort_v2(desordenada), sep=",")
    print(f'Tempo de processamento: {time.process_time() - start}')
