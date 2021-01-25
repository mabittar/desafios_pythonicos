def do_twice(f, n):
    f(n)
    f(n)


def print_span(arg):
    print(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_four(print_span, 'span')