from itertools import accumulate, combinations
from operator import add
from math import inf

"""
Mini - Max Sum
Data uma lista retorne a maior e menor soma possível das combinações de 4 elementos da list
"""

def max_min_calc(arr):
    max_sum = -inf
    min_sum = inf
    for c in combinations(arr, 4):
        max_sum = max(sum(c), max_sum)
        min_sum = min(sum(c), min_sum)
        
    return str(f"{min_sum} {max_sum}")


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')
    

if __name__ == '__main__':
    test(max_min_calc, [1, 2, 3, 4, 5], "10 14")
    test(max_min_calc, [1, 3, 5, 7, 9], "16 24")
    test(max_min_calc, [7, 69, 2, 221, 8974], "299 9271")
    