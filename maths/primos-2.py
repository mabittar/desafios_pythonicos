from functools import wraps
import math
from time import perf_counter


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = (perf_counter() - s)
            if elapsed < 1:
                elapsed = elapsed * 1000
                msg = f"{elapsed:0.4f} ms."
            else:
                msg = f"{elapsed:0.4f} s."
            print(f"Method: {func.__name__} executed in {msg}.")

    return wrapper

def trial_division(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def optimized_division(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

@timeit
def primes_sieve(n):
    prime, sieve = [], set()
    for q in range(2, n+1):
        if q not in sieve:
            prime.append(q)
            sieve.update(range(q*q, n+1, q))
    return prime

@timeit
def one_line(n):
    divisors = [d for d in range(2, n//2+1) if n % d == 0]
    return [d for d in divisors if
            all(d % od != 0 for od in divisors if od != d)]

@timeit
def find_primes(n, algorithm):
    primes = []
    for i in range(2, n +1):
        if algorithm(i):
            primes.append(i)
    return primes 


def informs(primes):
        print(f'primes found: {primes.__len__()}')
        print(f'last prime found: {primes[-1]}')
        print(f'larguest prime lenght found is: {len(str(primes[-1]))}')

if __name__ == '__main__':
    try:
        algorithms = [trial_division, optimized_division]
        # algorithms = [ primes_sieve1]
        n = 1000000
        for algo in algorithms:
            primes = find_primes(n=n, algorithm=algo)
            informs(primes)
        sieve = primes_sieve(n)
        informs(sieve)
        sieve = one_line(n)
        informs(sieve)
    
    except Exception as e:
        print(e)
    finally:
        print('Done!')