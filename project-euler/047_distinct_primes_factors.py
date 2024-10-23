#!/usr/bin/env python3

# https://projecteuler.net/problem=47


from functools import cache
from math import sqrt


@cache
def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_num_distinct_prime_factors(num: int) -> int:
    """
    Return the amount of distinct prime factors for a
    given number
    """
    factors = 0
    for possible_factor in range(1, num + 1):
        if is_prime(possible_factor) and num % possible_factor == 0:
            factors += 1
    return factors


def get_smallest_of_first_n_consecutive_numbers_with_n_distinct_prime_factors(
    n: int,
) -> int:
    """
    Return the smallest of the smallest set of `n`
    consecutive numbers which have `n` prime factors

    Examples:
        f(2) -> (14, 15) -> 14
        f(3) -> (644, 645, 646) -> 644
    """
    counter = 0
    len_consecutive_found = 0
    while True:
        if len_consecutive_found == n:
            return counter - n
        if get_num_distinct_prime_factors(counter) == n:
            len_consecutive_found += 1
            counter += 1
            continue
        len_consecutive_found = 0
        counter += 1


print(get_smallest_of_first_n_consecutive_numbers_with_n_distinct_prime_factors(2))
print(get_smallest_of_first_n_consecutive_numbers_with_n_distinct_prime_factors(3))
print(get_smallest_of_first_n_consecutive_numbers_with_n_distinct_prime_factors(4))
