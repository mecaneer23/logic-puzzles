#!/usr/bin/env python3
# https://projecteuler.net/problem=1


def get_sum_of_multiples_of_3_5_below(num: int) -> int:
    """
    Compute list of multiples of 3 or 5 below `num`.
    Return the sum of this list.

    Example: f(10) -> [3, 5, 6, 9] -> 23
    """
    return attempt_4(num)


def attempt_4(num: int) -> int:
    """
    Make attempt 3 actually work by accounting for multiples of 3 and 5
    """
    total = 0

    for i in range(0, num, 3):
        total += i

    for i in range(0, num, 5):
        if i % 3 == 0:
            continue
        total += i

    return total


def attempt_3(num: int) -> int:
    """
    Use two for loops, but don't iterate over unused values

    Potentially better performance because don't loop more than necessary

    DOESN'T WORK; doesn't account for multiples of 3 and 5
    """
    total = 0

    for i in range(0, num, 3):
        total += i

    for i in range(0, num, 5):
        total += i

    return total


def attempt_2(num: int) -> int:
    """
    Make a list using modulo, sum as you go

    Better because uses less space
    """
    total = 0

    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


def attempt_1(num: int) -> int:
    """Make a list using modulo, sum list at the end"""
    multiples: list[int] = []

    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)

    return sum(multiples)


print(get_sum_of_multiples_of_3_5_below(10))
print(get_sum_of_multiples_of_3_5_below(1000))
