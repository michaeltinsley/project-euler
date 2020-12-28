from math import sqrt
from typing import Set


def find_primes(value: int, prime_factors: Set[int]) -> Set[int]:
    """
    Appends prime factors to the set of prime factors.

    :param value: The input value
    :param prime_factors: The set of prime factors
    :return: The updated set of prime factors
    """
    for i in range(3, int(sqrt(value)) + 1, 2):
        while value % i == 0:
            value /= i
            prime_factors.add(i)

    if value > 2:
        prime_factors.add(value)

    return prime_factors


def find_all_prime_factors(value: int) -> Set[int]:
    """
    Finds all prime factors for a given value.

    :param value: The input value
    :return: A set of prime factors
    """
    prime_factors = set()

    while value % 2 == 0:
        prime_factors.add(2)
        value /= 2

    prime_factors = find_primes(value, prime_factors)

    return prime_factors


def largest_prime_factor(value: int) -> int:
    """
    Returns the largest prime factor in the given value.

    :param value: The input value
    :return: The largest prime factor of the given input value
    """
    return max(find_all_prime_factors(value))


if __name__ == "__main__":
    print(largest_prime_factor(13_195))
    print(largest_prime_factor(600_851_475_143))
