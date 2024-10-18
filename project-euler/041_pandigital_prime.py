#!/usr/bin/env python3
# https://projecteuler.net/problem=41


from math import sqrt


def is_pandigital(num: int) -> bool:
    """
    Return whether a given number uses all of the digits from 1 to its length once
    """
    num_str = str(num)
    return len(num_str) == len(set(num_str)) and all(
        str(i) in num_str for i in range(1, len(num_str) + 1)
    )


def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_largest_pandigital_prime() -> int:
    """
    Return the largest pandigital prime number
    """
    max_prime = 0
    counter = 2
    while True:
        if is_pandigital(counter) and is_prime(counter):
            max_prime = counter
        counter += 1
        if counter > 987_654_321:
            break
    return max_prime


print(get_largest_pandigital_prime())
