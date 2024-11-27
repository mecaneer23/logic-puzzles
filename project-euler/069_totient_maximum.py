#!/usr/bin/env python3

# https://projecteuler.net/problem=69

from functools import cache
from math import sqrt


@cache
def get_factors(num: int) -> set[int]:
    """Return a set of the factors of `num`"""
    factors: set[int] = set()
    for possible_factor in range(1, int(sqrt(num)) + 1):
        if num % possible_factor == 0:
            factors.add(possible_factor)
            factors.add(num // possible_factor)
    return factors


def totient(n: int) -> int:
    """
    Return the number of prime integers < `n`
    which don't have any shared factors with `n`
    other than `1`
    """
    factors_of_n = get_factors(n)
    total = 0
    for i in range(1, n):
        if factors_of_n & get_factors(i) == {1}:
            total += 1
    return total


def get_max_n_over_totient_n(upper_bound: int) -> int:
    """
    Return n which maximizes n/totient(n) <= upper_bound

    Example: f(10) -> 3 -> 6
    """
    max_totient = 0
    max_n = 0
    for n in range(2, upper_bound + 1):
        totient_n = n / totient(n)
        if totient_n > max_totient:
            max_totient = totient_n
            max_n = n
    return max_n


print(get_max_n_over_totient_n(10))
print(get_max_n_over_totient_n(1_000_000))
