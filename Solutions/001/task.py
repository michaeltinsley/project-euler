from typing import Generator, List, Tuple


def factor_generator(value: int) -> Generator[int, None, None]:
    """
    Finds all factors of a given value.

    :param value: The upper
    :return: A generator object
    """
    return (i for i in range(1, value + 1) if value % i == 0)


def multiple_of(multiple: int, value: int) -> bool:
    """

    :param multiple:
    :param value:
    :return:
    """
    return value % multiple == 0


def union_of_multiples(multiples: Tuple[int], upperbound: int) -> List[int]:
    """


    :param multiples:
    :param upperbound:
    :return:
    """
    all_factors = [
        set(range(0, upperbound, multiple)) for multiple in multiples
    ]
    return set().union(*all_factors)


def sum_multiples(multiples: Tuple[int], upperbound: int) -> None:
    """

    :param multiples:
    :param upperbound:
    :return:
    """
    intersection = union_of_multiples(multiples, upperbound)
    return sum(intersection)


if __name__ == "__main__":
    print(sum_multiples(multiples=(3, 5), upperbound=10))
    print(sum_multiples(multiples=(3, 5), upperbound=1000))
