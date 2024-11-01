#!/usr/bin/env python3

# https://projecteuler.net/problem=44

from functools import cache
from math import sqrt


@cache
def is_pentagonal(num: int) -> int:
    """
    Return whether a number is pentagonal
    """
    if num < 1:
        return False
    return ((1 + sqrt(1 + 24 * num)) / 6).is_integer()


def get_pentagon_difference() -> int:
    """
    Return the smallest positive difference
    of two pentagon numbers which have a
    sum and difference which are both also
    pentagonal
    """
    found_pentagonals: set[int] = set()
    counter = 1
    while True:
        pentagonal = (counter * (3 * counter - 1)) // 2
        counter += 1
        for found_num in found_pentagonals:
            if pentagonal - found_num in found_pentagonals and is_pentagonal(
                pentagonal + found_num
            ):
                return pentagonal - found_num
        found_pentagonals.add(pentagonal)


print(get_pentagon_difference())
