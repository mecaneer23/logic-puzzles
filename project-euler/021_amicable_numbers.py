#!/usr/bin/env python3

# https://projecteuler.net/problem=21

from functools import cache


@cache
def d(n: int) -> int:
    """
    Return sum of divisors of `n` excluding `n`

    Example: d(220) -> 284, d(284) -> 220"""
    total = 0
    for possible_factor in range(1, n):
        if n % possible_factor == 0:
            total += possible_factor
    return total


def sum_of_amicable_numbers_below(num: int) -> int:
    """
    Return the sum of all numbers below `num`
    where d(a) == b and d(b) == a and a != b
    """
    total = 0
    for i in range(1, num):
        if i == d(d(i)) and i != d(i):
            total += i
    return total


print(sum_of_amicable_numbers_below(10_000))
