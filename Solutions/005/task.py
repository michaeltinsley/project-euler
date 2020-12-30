from typing import Generator


def number_sequence_generator(multiple: int) -> Generator[int, None, None]:
    """
    An infinite number sequence generator for a given multiple

    :param multiple: The multiple value to return
    :return: The infinite multiple sequence
    """
    i = multiple
    while True:
        yield i
        i += multiple


def find_smallest_evenly_divisible_number(low: int, high: int) -> int:
    """
    Find the largest evenly divisible for the given range

    :param low: Minimum divisor range value
    :param high: Maximum divisor range value
    :return: The smallest evenly divisible number
    """
    divisor_range = range(high, low - 1, -1)

    for number_gen in number_sequence_generator(high):
        truthiness = [
            True if number_gen % divisor == 0 else False for divisor in divisor_range
        ]
        if all(truthiness):
            return number_gen


if __name__ == "__main__":
    print(find_smallest_evenly_divisible_number(1, 10))
    print(find_smallest_evenly_divisible_number(1, 20))
