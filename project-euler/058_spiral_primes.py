#!/usr/bin/env python3

# https://projecteuler.net/problem=058

from functools import cache
from math import sqrt


@cache
def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_smallest_square_spiral_with_ratio_below(percent: int) -> int:
    """
    Return the side length of the smallest square spiral where
    the ratio of primes on diagonal corners first falls below
    `percent`
    """
    corners_per_ring = 4
    size = 3
    corner_numbers: set[int] = set()
    corner_number = 1
    step = 2
    prime_count = 0
    total_corner_numbers = 0
    while True:
        for _ in range(corners_per_ring):
            corner_numbers.add(corner_number)
            corner_number += step
            total_corner_numbers += 1
        step += 2
        prime_count += sum(1 for num in corner_numbers if is_prime(num))
        spiral_prime_percent = prime_count * 100 / total_corner_numbers
        corner_numbers = set()
        if spiral_prime_percent <= percent:
            return size
        size += 2


print(get_smallest_square_spiral_with_ratio_below(10))
