def callable_gen(func):
    class CallableGen:
        def __init__(self, *args, **kwargs):
            self.gen = func(*args, **kwargs)

        def __next__(self):
            return self.gen.__next__()

        def __iter__(self):
            return self

        def __call__(self):
            return next(self)
    return CallableGen


@callable_gen
def FibGenerator():
    a = b = 1
    while True:
        a, b = b, a + b
        yield b


if __name__ == '__main__':
    fib = FibGenerator()
    for i in range(8):
        print(next(fib), end=' ')
    print('n', fib)
