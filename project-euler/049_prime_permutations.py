#!/usr/bin/env python3

# https://projecteuler.net/problem=49


from math import sqrt


def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_permutation(a: int, b: int) -> bool:
    """
    Return whether `a` and `b` are constructed
    from the same digits
    """
    return set(str(a)) == set(str(b))


def get_prime_permutations() -> list[str]:
    """
    Return all sequences of three four-digit
    primes, which are set apart by the same
    difference, and are permutations of one
    another

    Example: 1487 (+3330) 4817 (+3330) 8147 -> 148748178149
    """
    primes: list[int] = []
    for i in range(999, 10_000, 2):
        if is_prime(i):
            primes.append(i)

    prime_permutations: list[str] = []
    for i, first in enumerate(primes, start=1):
        for second in primes[i:]:
            third = second + (second - first)
            if (
                is_permutation(first, second)
                and third in primes
                and is_permutation(first, third)
            ):
                prime_permutations.append(f"{first}{second}{third}")
    return prime_permutations


print(get_prime_permutations())
