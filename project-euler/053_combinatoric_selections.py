#!/usr/bin/env python3

# https://projecteuler.net/problem=53

from math import comb


def is_n_choosing_r_sufficiently_large(n: int, r: int) -> bool:
    """
    Return whether the amount of ways to select r from n (nCr)
    is greater than 1_000_000
    """
    return comb(n, r) > 1_000_000


def get_combinatoric_selections() -> int:
    """
    Return the amount of nCr values greater than
    1_000_000 when 1 <= n <= 100 and r <= n
    """
    total = 0
    for n in range(23, 101):
        for r in range(1, n):
            if is_n_choosing_r_sufficiently_large(n, r):
                total += 1
                continue
    return total


print(get_combinatoric_selections())
