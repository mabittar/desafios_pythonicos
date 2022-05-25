import random

def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{0:{width}d} \t{0:{width}o} \t{0:{width}X} \t{0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    print_formatted(random.randint(2, 10))
