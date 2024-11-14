#!/usr/bin/env python3

# https://projecteuler.net/problem=63

from decimal import Decimal


def get_powerful_digit_counts() -> int:
    """
    Return the amount of positive integers that
    are `n`-digits long and can be represented by
    x raised to the `n`s
    """
    total = 0
    counter = 1
    n = 1
    while True:
        length = len(str(counter**n))
        if length > n:
            n += 1
            counter = 1
            continue
        if length == n:
            total += 1
        counter += 1
        if length > 100:  # TODO: fix arbitrary value
            return total


def attempt_1() -> int:
    """
    Return the amount of positive integers that
    are `n`-digits long and can be represented by
    x raised to the `n`s
    """
    total = 0
    counter = 1
    while True:
        if (counter ** (1 / Decimal(len(str(counter))))) % 1 == 0:
            print(counter, total)
            total += 1
        # TODO: when should the loop end and return total?
        counter += 1


print(get_powerful_digit_counts())
