#!/usr/bin/env python3

# https://projecteuler.net/problem=26

from decimal import Decimal, getcontext


def get_recurring_cycle_length(denominator: int) -> int:
    """
    Return the length of the recurring cycle of a
    fraction 1 / `denominator`

    Examples:
        f(5) -> 1/5 -> 0.2 -> 0
        f(6) -> 1/6 -> 0.166666 -> 1
        f(7) -> 1/7 -> 0.14285714285 -> 6
    """
    getcontext().prec = 5000  # TODO: fix arbitarily large amount of digits
    digits = (Decimal(1) / Decimal(denominator)).as_tuple().digits
    for start in range(len(digits)):
        pattern: list[int] = []
        for i, digit in enumerate(digits[start:]):
            if digits[i:i+len(pattern)] == tuple(pattern) and len(pattern) > 0:
                return len(pattern)
            pattern.append(digit)
    return 0


def get_longest_reciprocal_cycle_under(upper_bound: int) -> int:
    """
    Return the value of d < `upper_bound` where
    1/d contains the longest recurring cycle of
    digits in its decimal fraction part
    """
    max_len = 0
    max_denom = 0

    for denominator in range(2, upper_bound):
        length = get_recurring_cycle_length(denominator)
        if length > max_len:
            max_len = length
            max_denom = denominator
    return max_denom


print(get_longest_reciprocal_cycle_under(11))
print(get_longest_reciprocal_cycle_under(1000))
