import math


def primos(n):
    lista_fatores = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            # supposing you want multiple factors repeated
            lista_fatores.append(d)
            n //= d
        d += 1
    if n > 1:
        lista_fatores.append(n)
    return lista_fatores


def primes(n):
    divisors = [d for d in range(2, n//2+1) if n % d == 0]
    return [d for d in divisors if
            all(d % od != 0 for od in divisors if od != d)]


numero = 36
print(primos(numero))
print(primes(numero))
