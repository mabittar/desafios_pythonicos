"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""
from heapq import merge
lista=[]
def linear_merge(list1, list2):
    # +++ SUA SOLUÇÃO +++
    """ Solução 1 NAO LINEAR
        #lista para receber ordenado
        lista_final = []
        # percorre as listas
        while list1 and list2:
            # compara os valores
            if list1[0] <= list2[0]:
                item = list1.pop(0)
                lista_final.append(item)
            else:
                item = list2.pop(0)
                lista_final.append(item)
        # expande a lista final para receber os itens
        lista_final.extend(list1 if list1 else list2)
        return lista_final
    """
    # Solução 2 - LINEAR
    return sorted(merge(list1, list2))
# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
