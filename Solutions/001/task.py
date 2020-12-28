from typing import List, Optional, Tuple


def union_of_multiples(
    multiples: Tuple[int], upperbound: int, lowerbound: int
) -> List[int]:
    """
    Returns the union of a set of multiples.

    :param multiples: Specified multiple values
    :param upperbound: The upperbound limit
    :param lowerbound: The lowerbound limit
    :return: A set of the union of all multiples
    """
    all_factors = [
        set(range(lowerbound, upperbound, multiple)) for multiple in multiples
    ]
    return set().union(*all_factors)


def sum_union(
    multiples: Tuple[int], upperbound: int, lowerbound: Optional[int] = 0
) -> None:
    """
    Sums the union of multiples.

    :param multiples: Specified multiple values
    :param upperbound: The upperbound limit
    :param lowerbound: The lowerbound limit. Defaults to 0.
    :return: The sum of the union of all multiples
    """
    intersection = union_of_multiples(multiples, upperbound, lowerbound)
    return sum(intersection)


if __name__ == "__main__":
    print(sum_union(multiples=(3, 5), upperbound=10))
    print(sum_union(multiples=(3, 5), upperbound=1000))
