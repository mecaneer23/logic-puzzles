#!/usr/bin/env python3

# https://projecteuler.net/problem=heegner

from cmath import cos, pi, sqrt
from decimal import Decimal


def get_heegner_num() -> int:
    """
    Return the value n when cos(pi*sqrt(n)) is closest
    to an integer
    """
    min_diff = 1
    min_n = 0
    for n in range(-10**3, 10**3 + 1):
        square_root = sqrt(n)
        square_root = square_root.real + square_root.imag
        if square_root.is_integer():
            continue
        value = cos(Decimal(pi) * Decimal(square_root))
        value = value.real + value.imag
        difference = abs(value - round(value))
        if difference < min_diff:
            print(value, difference)
            min_diff = difference
            min_n = n
    return min_n


print(get_heegner_num())
