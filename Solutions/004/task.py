from typing import Generator, Iterable


def generate_palindromes(length: int) -> Generator[int, None, None]:
    """
    A palindromic integer generator in decreasing order

    :param length: The digit length of the palindromic integer
    :return: A palindromic integer of the given length
    """
    even = True if length % 2 == 0 else False
    split = int(length / 2 if even else (length - 1) / 2)

    start_value = int("9" * split)
    end_value = int("9" * (split - 1))

    for value in range(start_value, end_value, -1):
        if even:
            yield int(f"{value}{str(value)[::-1]}")
        else:
            for middle_value in range(9, 0, -1):
                yield int(f"{value}{middle_value}{str(value)[::-1]}")


def find_integer_multiples(product: int, input_range: Iterable[int]) -> bool:
    """
    Asserts if a given value is a product of two integer numbers within a given
    range.

    :param product: The product value to check against
    :param input_range: An iterable of the range of values to check
    :return: True if input product is a product of two values in input_range,
             False otherwise
    """
    for i in input_range:
        if (product % i == 0) and (product / i in input_range):
            print(f"{i} * {int(product/i)} = {product}")
            return True
    return False


def find_largest_palindromic_product(input_length: int) -> int:
    """
    Finds the largest palindromic number that is a product of two number of
    the input_length digits

    :param input_length: The digit length
    :return: The highest palindromic integer
    """
    start_value = int("9" * (input_length - 1))
    end_value = int("9" * input_length)
    multiple_range = range(start_value + 1, end_value + 1)

    for palindrome in generate_palindromes(2 * input_length):
        if find_integer_multiples(palindrome, multiple_range):
            return palindrome


if __name__ == "__main__":
    print(find_largest_palindromic_product(2))
    print(find_largest_palindromic_product(3))
