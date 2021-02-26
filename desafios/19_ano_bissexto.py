""" 
anos bissextos são aqueles que são múltiplos de 4, como 1996, 2000, 2004 etc 
(que podem ser divididos por 4 deixando resto 0).
Porém, há uma exceção: múltiplos de 100 que não sejam múltiplos de 400.

Uma das duas condições a seguir deve ser verdadeira:
Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)
"""
def bissexto(ano):
    if ano % 4 == 0 or ano % 100 != 0 and ano % 400 == 0:
        return True
    return False


assert all(bissexto(n) for n in (1996, 2000, 2004))
assert not (all(bissexto(n) for n in (2001, 2002, 2003, 2005)))

