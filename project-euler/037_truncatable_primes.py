#!/usr/bin/env python3

# https://projecteuler.net/problem=37


from math import sqrt


def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_truncatable_prime(num: int) -> bool:
    """Check if a prime number remains prime when truncated"""
    prime = str(num)
    length = len(prime)
    if length == 1 or not is_prime(num):
        return False
    for i in range(1, length):
        if not is_prime(int(prime[i:])) or not is_prime(int(prime[:-i])):
            return False
    return True


def truncatable_primes() -> int:
    """
    Return the sum of the 11 primes that remain
    prime when truncated from either end
    """
    total = 0
    primes_found = 0
    prime = 0
    while True:
        if primes_found >= 11:
            break

        if is_truncatable_prime(prime):
            primes_found += 1
            total += prime
        prime += 1
    return total


print(truncatable_primes())
