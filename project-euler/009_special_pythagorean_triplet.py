#!/usr/bin/env python3
"""https://projecteuler.net/problem=9"""


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    """
    Returns whether (a, b, c) is a valid Pythagorean triplet

    A valid Pythagorean triplet is a set of three natural numbers
    `a` < `b` < `c` for which `a`^2 + `b`^2 = `c`^2
    """
    return a < b < c and a**2 + b**2 == c**2


def special_pythagorean_triplet(target: int) -> int:
    """
    Find the product of the pythagorean triplet
    for which `a` + `b` + `c` = `target`

    Example: f(12) -> 3 + 4 + 5 -> 3^2 + 4^2 = 5^2 -> 3 * 4 * 5 -> 60
    Example: f(1000) -> 200 + 375 + 425 -> 200^2 + 375^2 = 425^2 -> 200 * 375 * 425 -> 31875000
    """
    return brute_force(target)


def brute_force(target: int) -> int:
    """Manually iterate over all possible targets to find a solution"""
    for c in range(target, 1, -1):
        for a in range(target):
            for b in range(target):
                if a + b + c == target and is_pythagorean_triplet(a, b, c):
                    return a * b * c
    return 0


print(special_pythagorean_triplet(12))
print(special_pythagorean_triplet(1000))
