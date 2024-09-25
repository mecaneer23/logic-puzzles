#!/usr/bin/env python3

# https://projecteuler.net/problem=5


def get_least_common_factor(num_1: int, num_2: int) -> int:
    """Returns the least common factor between two numbers"""

    a = num_1
    b = num_2
    if num_1 < num_2:
        a = num_2
        b = num_1

    for i in range(1, a):
        if (i * a) % b == 0:
            return i * a
    return a * b


def smallest_multiple_from_1_to(bound: int) -> int:
    """
    Returns the smallest number that can be divided by
    each number from 1 to `bound` (inclusive) without
    a remainder.

    Example: f(10) -> 2520
    """

    total = bound
    for i in range(bound, 0, -1):
        total = get_least_common_factor(total, i)
    return total


print(smallest_multiple_from_1_to(10))
print(smallest_multiple_from_1_to(20))
