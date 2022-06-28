"""
Dada uma lista de caracteres (strings), retorne o número de vezes que a sequencia aparace na
lista queries.

"""

def count_strings(strings: list, queries: list):
    # result = []
    # count = 0
    # for q in queries:
    #     result.append(strings.count(q))
    result = [strings.count(q) for q in queries]
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
    test(count_strings, (["aba", "baba", "aba", "xzb"], ["aba", "xzb", "ab"]), [2, 1 ,0])
    