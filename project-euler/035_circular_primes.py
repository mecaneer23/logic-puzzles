#!/usr/bin/env python3

# https://projecteuler.net/problem=35

from itertools import permutations
from math import sqrt


def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_circular_prime(num: int) -> bool:
    """Returns whether a given number is a circular prime"""
    if not is_prime(num):
        return False
    for permutation in permutations(str(num)):
        possible_prime = 0
        for idx, digit in enumerate(reversed(permutation)):
            possible_prime += int(digit) * 10**idx
        if not is_prime(possible_prime):
            return False
    return True


def get_amount_of_circular_primes_below(num: int) -> int:
    """
    Return the amount of circular primes below `num`, where
    a circular prime is a prime number that remains prime
    for all rotations of its digits

    Example: f(100) -> 13
    """
    count = 0
    for i in range(num):
        if is_circular_prime(i):
            count += 1
    return count


print(get_amount_of_circular_primes_below(100))
print(get_amount_of_circular_primes_below(1_000_000))
