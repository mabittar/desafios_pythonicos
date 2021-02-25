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

# versão funcionando
# def sum_of_squares(n):
#     string = str(n)
#     digits = [int(char) ** 2 for char in string]
#     return sum(digits)


# def happy(n):
#     box = []
#     while n != 1 and n not in box:
#         box.append(n)
#         n = sum_of_squares(n)
#     return n == 1

def sum_of_squares(n):
    return sum([int(char) ** 2 for char in str(n)])


def happy(n):
    if n < 10:
        return n in (1, 7)
    return happy(sum_of_squares(n))


assert all(happy(n) for n in (1, 10, 97, 100, 130))
# assert happy(1)
# assert happy(10)
# assert happy(97)
# assert happy(100)
# assert happy(130)

# para consultar quais números não são felizes:
# abra o terminal e importe o módulo happy
# [(n, happy(n)) for n in range(1, 10)]
# [(1, True), (2, False), (3, False), (4, False), (5, False), (6, False), (7, True), (8, False), (9, False)]
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
