from itertools import combinations


def get_sums(input: list, target: int):
    """Os elementos deverão ser somados ao pares A[i] + A[j].
    Deverá retornar a somatória mais próxima do alvo.

    Args:
        input (list): list de inteiros a serem somados
        target (int): valor alvo a ser comparado
    """
    somatoria_pares = set()
    pares = []
    for seq in combinations(input, 2):
        if sum(seq) not in somatoria_pares and sum(seq) <= target:
            pares.append(seq)
        somatoria_pares.add(seq)
    print(f"Pares: {pares}")
    result = max(sum(par) for par  in pares) if len(pares) > 0 else -1
    return result
    
    


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_[0], in_[1])

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(get_sums, ([1, 2, 3], 3), 3)
    test(get_sums, ([1, 2, 2, 3, 4, 4, 1], 10), 8)
    test(get_sums, ([1, 2, 2, 3, 4, 4, 17, 21, 32, 1], 10), 8)