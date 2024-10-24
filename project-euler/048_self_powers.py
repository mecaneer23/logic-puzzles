#!/usr/bin/env python3

# https://projecteuler.net/problem=48


def get_series(maximum: int) -> int:
    """
    Return the sum of the series
    `1^1 + 2^2 + 3^3 + ... + maximum^maximum`
    """
    total = 0
    for i in range(1, maximum + 1):
        total += i**i
    return total


def get_last_n_digits_of_number(num: int, n: int) -> str:
    """
    Return the last `n` digits of the given number
    """
    return str(num)[-n:]


print(get_series(10))
print(get_last_n_digits_of_number(get_series(1000), 10))
