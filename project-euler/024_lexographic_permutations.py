#!/usr/bin/env python3

# https://projecteuler.net/problem=24

from itertools import permutations


def get_lexographic_permutations() -> int:
    """
    Return the millionth lexographic permutation
    of the digits 0-9 inclusive
    """
    for index, permutation in enumerate(permutations(range(10)), start=1):
        if index == 1_000_000:
            final_num = 0
            for idx, digit in enumerate(reversed(permutation)):
                final_num += digit * 10**idx
            return final_num
    return 0


print(get_lexographic_permutations())
