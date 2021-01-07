"""
14. Maior Intervalo

Neste desafio você a partir de uma lista dada você deverá 
retornar o maior interalo contínuo da sequência de números.

por exemplo:
input: [11, 7, 4, 2, 0, 1]
output:[0,4]

Dica: ordenar a sequência dad é uma maneira, entretando toma-se 
muito recursos e tempo (O log (n)), existe uma maneira linear de 
executar esse algorítmo.

Dica: no Python há o recurso de hashtables
"""

def maior_intervalo(matriz):
# --- Escreva seu código aqui. ---
    numeros = { x:0 for x in matriz}
    esquerda = direita = 0

    for numero in matriz:
        if numeros[numero] == 0:
            contador_d = numero + 1
            contador_e = numero - 1

        while contador_e in numeros:
            numeros[contador_e] = 1
            contador_e -= 1
        contador_e += 1

        while contador_d in numeros:
           numeros[contador_d] = 1
           contador_d += 1
        contador_d -= 1

        if (direita - esquerda) <= (contador_d - contador_e):
            direita = contador_d
            esquerda = contador_e

    return [esquerda, direita]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


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
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(maior_intervalo, [11, 7, 3, 4, 0, 2, 1], [0,4])
    test(maior_intervalo, [22, 20, 30, 39, 31, 21, 41, 23], [20,23])
    test(maior_intervalo, [1, 7, 6, 5, 0, 3, 2, 8, 9, 10], [5,10])


