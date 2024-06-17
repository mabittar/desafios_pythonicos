from multiprocessing import Process, Manager
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

@timeit
def primes_sieve(time_limit, return_dict):
    prime, sieve = [], set()
    start_time = time()
    q = 2
    while (time() - start_time) < time_limit:
        if q not in sieve:
            prime.append(q)
            for multiple in range(q * q, int(q * q + time_limit * 10000), q):
                sieve.add(multiple)
        q += 1
    return_dict['sieve'] = prime

@timeit
def segmented_sieve(time_limit, return_dict):
    start_time = time()
    limit = 1000000  # this can be adjusted based on the memory constraints
    primes = []
    low = 2
    high = limit

    while (time() - start_time) < time_limit:
        sieve = [True] * (high - low + 1)

        for i in range(2, int(math.sqrt(high)) + 1):
            start = max(i * i, (low + i - 1) // i * i)
            for j in range(start, high + 1, i):
                sieve[j - low] = False

        for i in range(low, high + 1):
            if sieve[i - low]:
                primes.append(i)

        low += limit
        high += limit

    return_dict['segmented_sieve'] = primes

def informs(primes, method):
    print(f'{method} primes found: {len(primes)}')
    print(f'{method} last prime found: {primes[-1] if primes else "None"}')
    print(f'{method} largest prime length found is: {len(str(primes[-1])) if primes else "None"}')


if __name__ == '__main__':
    try:
        time_limit = 30  # seconds
        manager = Manager()
        return_dict = manager.dict()

        sieve_process = Process(target=primes_sieve, args=(time_limit, return_dict))
        segmented_sieve_process = Process(target=segmented_sieve, args=(time_limit, return_dict))

        sieve_process.start()
        segmented_sieve_process.start()

        sieve_process.join()
        segmented_sieve_process.join()

        sieve_primes = return_dict.get('sieve', [])
        segmented_sieve_primes = return_dict.get('segmented_sieve', [])

        informs(sieve_primes, 'Sieve of Eratosthenes')
        informs(segmented_sieve_primes, 'Segmented Sieve')

    except Exception as e:
        print(e)
    finally:
        print('Done!')
