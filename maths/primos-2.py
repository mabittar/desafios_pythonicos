from functools import wraps
import math
from time import perf_counter, time


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
def primes_sieve(time_limit):
    prime, sieve = [], set()
    start_time = time()
    q = 2
    while (time() - start_time) < time_limit:
        if q not in sieve:
            prime.append(q)
            for multiple in range(q * q, int(q * q + time_limit * 10000), q):
                sieve.add(multiple)
        q += 1
    return prime

def one_line(time_limit):
    start_time = time()
    primes = []
    n = 2
    while (time() - start_time) < time_limit:
        divisors = [d for d in range(2, n // 2 + 1) if n % d == 0]
        if not divisors:
            primes.append(n)
        n += 1
    return primes

def find_primes_within_time_limit(time_limit, algorithm):
    primes = []
    start_time = time()
    n = 2
    while (time() - start_time) < time_limit:
        if algorithm(n):
            primes.append(n)
        n += 1
    return primes

def informs(primes):
    print(f'primes found: {len(primes)}')
    print(f'last prime found: {primes[-1]}')
    print(f'largest prime length found is: {len(str(primes[-1]))}')

@timeit
def run_algorithm(time_limit, algorithm, is_sieve=False):
    if is_sieve:
        primes = algorithm(time_limit)
    else:
        primes = find_primes_within_time_limit(time_limit, algorithm)
    informs(primes)
    return primes

if __name__ == '__main__':
    try:
        algorithms = [
            (one_line, False),
            (trial_division, False),
            (optimized_division, False),
            (primes_sieve, True)
        ]
        time_limit = 30  # seconds
        for algo, is_sieve in algorithms:
            run_algorithm(time_limit, algo, is_sieve)
    except Exception as e:
        print(e)
    finally:
        print('Done!')