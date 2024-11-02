#!/usr/bin/env python3

# https://projecteuler.net/problem=38


def get_large_pandigital_multiple() -> int:
    """
    Return the largest 1-9 pandigital number that can be formed as the
    concatenated product of an integer with (1, 2, ..., n)
    """
    for counter in range(10_000, 2, -1):
        n = 1
        current = ""
        while len(current) < 9:
            current += str(counter * n)
            n += 1
        if len(current) == 9 and set(current) == set("123456789"):
            return int(current)
    return 0


print(get_large_pandigital_multiple())
