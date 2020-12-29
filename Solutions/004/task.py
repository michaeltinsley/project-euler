from typing import Generator


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


if __name__ == "__main__":
    for i in generate_palindromes(6):
        print(i)
