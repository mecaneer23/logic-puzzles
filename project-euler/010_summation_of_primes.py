#!/usr/bin/env python3

# https://projecteuler.net/problem=10


from math import sqrt


# Refer to solution to 007...
def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_sum_of_primes_below(num: int) -> int:
    """
    Return the sum of all prime numbers less than `num`

    Example: f(10) -> (2, 3, 5, 7) -> 17
    """
    total = 0

    for i in range(2, num):
        if is_prime(i):
            total += i
    return total


print(get_sum_of_primes_below(10))
print(get_sum_of_primes_below(2_000_000))
