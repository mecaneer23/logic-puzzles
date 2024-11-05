#!/usr/bin/env python3

# https://projecteuler.net/problem=057

from fractions import Fraction


def get_square_root_convergents() -> int:
    """
    Return the amount of fractions in the infinite continued
    function which forms sqrt(2) where the length of digits
    of the numerator is greater than the length of digits of
    the denominator (for the first 1000 expansions)
    """
    total = 0
    current = Fraction(1, 2)
    for _ in range(1, 1_000):
        current = Fraction(1, 2 + current)
        numerator, denominator = (1 + current).as_integer_ratio()
        if len(str(numerator)) > len(str(denominator)):
            total += 1
    return total


print(get_square_root_convergents())
