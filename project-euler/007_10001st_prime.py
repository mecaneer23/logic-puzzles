#!/usr/bin/env python3
"""
I don't know if there's a non-brute-force way to implement this...

https://projecteuler.net/problem=7
"""

from math import sqrt


def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_nth_prime(num: int) -> int:
    """
    Return the `num`th prime number

    Example: f(6) -> [2, 3, 5, 7, 11, 13] -> 13
    """
    primes_found = 0
    counter = 1

    while True:
        counter += 1
        if is_prime(counter):
            primes_found += 1
        if primes_found == num:
            return counter


print(get_nth_prime(6))
print(get_nth_prime(10_001))
