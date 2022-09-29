def fibonacci():
    current, next = 0, 1
    while True:
        yield current
        current, next = next, current + next


def main(repetitions: int):
    """
    the fibonacci function above is a generator function which returns a generator iterator, 
    and next() is Pythons built-in function for manually advancing through any sort of iterable object, not just generators. For iterables which eventually halt, 
    an exception called StopIteration is raised to tell you to, well, stop iterating.
    """
    f = fibonacci()
    for i in range(repetitions):
        print(next(f))


if __name__ == '__main__':
    main(150)
