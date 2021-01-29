""" 
 dado um número inteiro positivo
 substitua o número pela soma dos quadrados dos seus dígitos
 se o resultado for 1 o número é feliz
 caso contrário repita o processo

 exemplos:
 o número 7 é feliz?
 7² = 49
 4² + 9² = 97
 9² + 7² = 130
 1² + 3² + 0² = 10
 1² + 0² = 1

 portanto 7 é feliz

"""


def sum_square(n):
    digits = [int(char) ** 2 for char in str(n)]
    return sum(digits)


def happy(n):
    if n < 10:
        return n in (1, 7)
    return happy(sum_square(n))


if __name__ == '__main__':
    assert all([happy(n) for n in (1, 10, 100, 97, 130)])

    assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
