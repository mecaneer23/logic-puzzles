#!/usr/bin/env python3

# https://projecteuler.net/problem=52


def get_permuted_multiples() -> int:
    """
    Return the smallest positive integer `x`
    where `2x`, `3x`, `4x`, `5x`, and `6x` all
    contain the same digits
    """
    x = 1
    found = 1
    amount_to_find = 6
    while True:
        for n in range(1, amount_to_find + 1):
            nx = str(n * x)
            str_x = str(x)
            if len(nx) != len(str_x) or set(nx) != set(str_x):
                found = 1
                break
            found += 1
        if found >= amount_to_find:
            return x
        x += 1


print(get_permuted_multiples())
