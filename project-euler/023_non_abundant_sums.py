#!/usr/bin/env python3

# https://projecteuler.net/problem=23

def get_factor_sum(num: int) -> int:
    """
    Return the sum of factors of a number
    """
    total = 0
    for possible_factor in range(1, num):
        if num % possible_factor == 0:
            total += possible_factor
    return total


def get_abundant_numbers() -> set[int]:
    """Return set of all positive abundant numbers less than 28,123"""
    abundant_numbers: set[int] = set()
    for i in range(1, 28_123 + 1):
        if get_factor_sum(i) > i:
            abundant_numbers.add(i)
    return abundant_numbers


def get_non_abundant_sum() -> int:
    """
    Return the sum of all positive integers which
    cannot be written as the sum of two numbers which
    have a sum of factors greater than themselves
    """
    abundant_numbers = get_abundant_numbers()

    total = 0
    for i in range(1, 28_123 + 1):
        for abundant in abundant_numbers:
            if i - abundant in abundant_numbers:
                break
        else:  # TODO: refactor to avoid using for-else
            total += i
    return total


print(get_non_abundant_sum())
