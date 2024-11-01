#!/usr/bin/env python3

# https://projecteuler.net/problem=45

from math import sqrt


def is_pentagonal(num: int) -> bool:
    """
    Return whether a number is pentagonal

    True examples: 1, 5, 12, 22, 35
    """
    return ((1 + sqrt(1 + 24 * num)) / 6).is_integer()


def is_hexagonal(num: int) -> bool:
    """
    Return whether a number is hexagonal

    True examples: 1, 6, 15, 28, 45
    """
    return ((1 + sqrt(1 + 8 * num)) / 4).is_integer()


def get_tri_pent_hex_numbers(n: int) -> int:
    """
    Return the `n`th number which is triangular, pentagonal, and hexagonal
    """
    counter = 1
    while True:
        tri_num = counter * (counter + 1) // 2
        if is_pentagonal(tri_num) and is_hexagonal(tri_num):
            n -= 1
        if n == 0:
            return tri_num
        counter += 1


print(get_tri_pent_hex_numbers(3))
