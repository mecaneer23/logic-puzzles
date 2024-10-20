#!/usr/bin/env python3

# https://projecteuler.net/problem=43

from itertools import permutations


def is_divisible(pandigital: int) -> bool:
    """
    Return whether the given pandigital number's substrings
    are divisible by ascending initial primes

    Example: f(1406357289) -> True
    """
    primes = (1, 2, 3, 5, 7, 11, 13, 17)
    for i in range(8):
        if int(str(pandigital)[i : i + 3]) % primes[i] != 0:
            return False
    return True


def pandigital_divisible_sum() -> int:
    """
    Return the sum of all 0-9 pandigital numbers
    for which each substring of 3 digits is
    divisible by ascending initial primes
    """
    total = 0

    for permutation in permutations(range(10)):
        pandigital = 0
        for idx, digit in enumerate(reversed(permutation)):
            pandigital += int(digit) * 10**idx
        if is_divisible(pandigital):
            total += pandigital

    return total


print(pandigital_divisible_sum())
