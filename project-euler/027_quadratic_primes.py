#!/usr/bin/env python3

# https://projecteuler.net/problem=27

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


def get_primes_from_quadratic(coef_n: int, coef: int) -> int:
    """
    Return the amount of primes 0 <= x found by plugging in
    consecutive values to the equation `n^2 + coef_n*n + coef`

    Example: f(1, 41) -> 40
    """
    n = 0
    while True:
        if not is_prime(n * n + coef_n * n + coef):
            return n
        n += 1


def get_max_prime_quadratic_coefficient_product() -> int:
    """
    Return the product of the coefficients that yield
    the maximum consecutive prime values
    """
    max_primes = 0
    product = 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            primes = get_primes_from_quadratic(a, b)
            if primes > max_primes:
                max_primes = primes
                product = a * b
    return product


print(get_max_prime_quadratic_coefficient_product())
