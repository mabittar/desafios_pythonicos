
def FibGenerator():
    """Ao contrário de uma função normal, 
    uma função geradora não executa nenhum código dentro dela quando chamamos a função. 
    Em vez disso, ele constrói um objeto gerador e o retorna.
    """
    a = b = 1
    while True:
        a, b = b, a + b
        yield b


if __name__ == '__main__':
    fib = FibGenerator()
    for i in range(8):
        print(next(fib), end=' ')
    print('n', fib)
