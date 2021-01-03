import itertools


def sieve_of_eratosthenes() -> int:
    """
    An efficient prime number generator.

    :return: All prime numbers
    """
    yield 2

    cache = {}
    n = 3

    while True:
        if p := cache.pop(n, None):
            x = p + n
            while x in cache:
                x += p
            cache[x] = p
        else:
            cache[n * n] = 2 * n
            yield n
        n += 2


def find_prime(index: int) -> int:
    """
    Finds the nth prime number, where 2 is the 1st prime number.

    :param index: The index value of the desired prime
    :return: The prime number
    """
    prime_generator = sieve_of_eratosthenes()
    return next(itertools.islice(prime_generator, index - 1, None))


if __name__ == "__main__":
    print(find_prime(6))
    print(find_prime(10_001))
