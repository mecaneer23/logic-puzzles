#!/usr/bin/env python3

# https://projecteuler.net/problem=28


def get_number_spiral_diagonal_sum(size: int) -> int:
    """
    Return the sum of the diagonal numbers in a `size` x `size`
    clockwise spiral starting from the middle

    Example: f(5) -> 101
    """
    corners_per_ring = 4
    total = 0
    corner_number = 1
    step = 2
    corners_counted = 0
    while True:
        total += corner_number
        corner_number += step
        corners_counted += 1
        if corners_counted == corners_per_ring:
            step += 2
            corners_counted = 0
        if corner_number > size**2:
            break
    return total


print(get_number_spiral_diagonal_sum(5))
print(get_number_spiral_diagonal_sum(1001))
