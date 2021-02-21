# Source: Automate the Boring stuff with python Ch. 4 Project

def join_code(items, sep):
    """essa função junta os itens da lista items utilizando a sep para separá-os

    Args:
        items (lista): lista de itens a ser juntados
        sep (símbolo): símbolo a ser utilizado na união dos itens, exemplos: ',' , '\n', ';'.

    Returns:
        [lista]: lista de itens unificados
    """
    items_len = len(items)

    if items_len == 0:
        return ''

    elif items_len == 1:
        return items[0]

    SEP = str(sep)
    if SEP == "\n":
        return SEP.join(items[:-1]) + ' e ' + SEP + items[-1]
    else:
        return SEP.join(items[:-1]) + ' e ' + items[-1]


if __name__ == '__main__':
    lista = ['gato', 'cachorro', 'pássaro', 'coelho']
    print(join_code(lista, ' \n'))
    print(join_code(lista, ', '))
