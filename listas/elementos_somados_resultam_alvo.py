from itertools import combinations


def get_sums(input: list, target: int): 
    """ 
    Encontre toda as combinações de soma dos elementos da lista que resultam o valor alvo.
    dada uma lista de inteiros, quais as combinações de soma possíveis que retornam o valor do alvo
    input: Lista de inteiros
    targer: inteiro maior que zero

    exemplos:
    [1, 2, 3], 3 -> [(1, 2), (3)]
    [1, 2 ,2, 3, 4 ,4, 1], 5 -> 

    """
    result = [seq for i in range(len(input), 0, -1)
                for seq in combinations(input, i)
                if sum(seq) == target]

    print(result)
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
    test(get_sums, ([1, 2, 3], 3), [(1, 2), (3,)])
    test(get_sums, ([1, 2, 2, 3, 1], 5), [(1, 2, 2), (1, 3, 1), (2, 2, 1), (2, 3), (2, 3)])
    test(
        get_sums, (
            [1, 2, 2, 3, 4, 4, 1], 10),
        [(1, 2, 2, 4, 1),
         (1, 2, 2, 4, 1),
         (1, 2, 3, 4),
         (1, 2, 3, 4),
         (1, 2, 3, 4),
         (1, 2, 3, 4),
         (1, 4, 4, 1),
         (2, 3, 4, 1),
         (2, 3, 4, 1),
         (2, 3, 4, 1),
         (2, 3, 4, 1),
         (2, 4, 4),
         (2, 4, 4)])
