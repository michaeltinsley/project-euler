from typing import Generator


def even_fibonacci_generator(
    first_val: int, second_val: int, max_value: int
) -> Generator[int, None, None]:
    """
    Returns an infinite Fibonacci sequence generator of only the even values.

    :param first_val: The first starting value
    :param second_val: The second starting value
    :param max_value: The upperbound limit
    :return: An infinite Fibonacci sequence generator
    """
    while True:
        if first_val % 2 == 0:
            yield first_val
        first_val, second_val = second_val, first_val + second_val
        if first_val > max_value:
            return


def sum_even_values(first_val: int, second_val: int, max_value: int) -> int:
    """
    Finds the sum of all even Fibonacci numbers up to a given max value

    :param first_val: The first starting value
    :param second_val: The second starting value
    :param max_value: The upperbound limit
    :return: The summation of the valid Fibonacci numbers
    """
    fibonacci_gen = even_fibonacci_generator(first_val, second_val, max_value)
    return sum(value for value in fibonacci_gen)


if __name__ == "__main__":
    print(sum_even_values(1, 2, 10))
    print(sum_even_values(1, 2, 4_000_000))
