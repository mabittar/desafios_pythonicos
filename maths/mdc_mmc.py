def mdc(a, b):
    """máximo divisor comum entre dois números
    em inglês: GCD (Greatest Common Divisor) or HCF (Highest Common Factor) 
    Args:
        a (inteiro): 
        b (inteiro)

    Returns:
        inteiro: correspondente ao maior número divisível entre dois ou mais números inteiros.

Lembre-se que os números divisores são aqueles que ocorrem quando o resto da divisão é igual a zero. 
Por exemplo, o número 12 é divisível por 1, 2, 3, 4, 6 e 12. Se dividirmos esses números pelo 12 obteremos 
um resultado exato, sem que haja um resto na divisão.
Quando um número tem apenas dois divisores, ou seja, ele é divisível somente por 1 e por ele mesmo, 
eles são chamados de números primos.
Vale notar que todo número natural possui divisores. 
O menor divisor de um número será sempre o número 1. Por sua vez, o maior divisor de um número é o próprio número.
    """
    if (b == 0):
        return a
    if (a == 0):
        return b
    else:
        return mdc(b, a % b)


def mmc(a, b):
    """mínimo multiplo comum entre dois números
    ou LCM - Last Commun Multiple
    Args:
        a (inteiro)
        b (inteiro):

Correspondente ao menor número inteiro positivo, diferente de zero, que é múltiplo ao mesmo tempo de dois ou mais números.
Lembre-se que para encontrar os múltiplos de um número, basta multiplicar esse número pela sequência dos números naturais.
Note que o zero (0) é múltiplo de todos os números naturais e que os múltiplos de um número são infinitos.
Para saber se um número é múltiplo de um outro, devemos descobrir se um é divisível pelo outro.
Por exemplo, 25 é múltiplo de 5, pois ele é divisível por 5.
    """
    return (a / mdc(a, b)) * b


def test(f, a, b, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(a, b)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({a!r}, {b!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(mdc, 36, 60, 12)
    test(mdc, 20, 28, 4)
    test(mdc, 98, 56, 14)

    test(mmc, 2, 3, 6)
    test(mmc, 12, 45, 180)
    test(mmc, 0, 6, 6)
