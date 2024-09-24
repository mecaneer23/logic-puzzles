#!/usr/bin/env python3
# https://projecteuler.net/problem=3

from math import sqrt


def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def largest_prime_factor(num: int) -> int:
    """
    Prime factorize a number and return the greatest prime factor.
    Return 1 if the number is prime.

    Example: 13195 -> [5, 7, 13, 29] -> 29

    I did some research on Pollard and Strassen methods and
    decided while they might be optimal, they seems complicated,
    so I'll use a simpler (basically brute-force) algorithm.
    """

    for potential_factor in range(int(sqrt(num) + 1), 1, -1):
        if is_prime(potential_factor) and num % potential_factor == 0:
            return potential_factor
    return 1


print(largest_prime_factor(13195))
print(largest_prime_factor(17))
print(largest_prime_factor(600_851_475_143))
