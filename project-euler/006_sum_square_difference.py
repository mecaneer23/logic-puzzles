#!/usr/bin/env python3

# https://projecteuler.net/problem=6


def sum_square_difference(num: int) -> int:
    """
    Returns the difference between the sum of the
    squares of whole numbers between 1^2 and `num`^2,
    and the square of the sum of whole numbers between
    1 and `num`.

    Example: f(10) -> (3025, 385) -> 2640
    """
    # calculate square of sums
    total = ((num + 1) * num // 2) ** 2

    # subtract each square (sum of squares)
    for i in range(1, num + 1):
        total -= i**2

    return total


print(sum_square_difference(10))
print(sum_square_difference(100))
