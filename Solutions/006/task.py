from typing import Iterable


def sum_of_squares(values: Iterable[int]) -> int:
    """
    Calculates the sum of squares for a given input iterable.

    :param values: The input iterable
    :return: The calculated output integer
    """
    return sum([x * x for x in values])


def square_of_sum(values: Iterable[int]) -> int:
    """
    Calculates the square of sums for a given input iterable.

    :param values: The input iterable
    :return: The calculated output integer
    """
    return pow(sum(values), 2)


def difference(n: int) -> int:
    """
    Finds the difference between the square of sums and the sum of squares.

    :param n: The number of values to compute
    :return: The calculated difference
    """
    input_values = range(1, n + 1)

    sum_squares = sum_of_squares(input_values)
    square_sums = square_of_sum(input_values)
    return square_sums - sum_squares


if __name__ == "__main__":
    print(difference(10))
    print(difference(100))
