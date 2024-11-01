#!/usr/bin/env python3

# https://projecteuler.net/problem=46

from math import sqrt
from functools import cache


@cache
def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def can_be_sum_of_prime_and_twice_square(num: int) -> bool:
    """
    Return whether a given number can be expressed as a sum
    of a prime number and 2 * a square
    """
    possible_prime = num - 2
    while True:
        if is_prime(possible_prime):
            if sqrt((num - possible_prime) // 2).is_integer():
                return True
        possible_prime -= 2
        if possible_prime < 2:
            return False


def smallest_odd_composite_not_sum_prime_and_twice_square() -> int:
    """
    Return the smallest odd composite number which is not a sum
    of a prime number and 2 * a square
    """
    counter = 3
    while True:
        if not is_prime(counter) and not can_be_sum_of_prime_and_twice_square(counter):
            return counter
        counter += 2


print(smallest_odd_composite_not_sum_prime_and_twice_square())
