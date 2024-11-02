#!/usr/bin/env python3

# https://projecteuler.net/problem=26

from decimal import Decimal


def get_recurring_cycle_length(denominator: int) -> int:
    """
    Return the length of the recurring cycle of a
    fraction 1 / `denominator`

    Examples:
        f(5) -> 1/5 -> 0.2 -> 0
        f(6) -> 1/6 -> 0.166666 -> 1
        f(7) -> 1/7 -> 0.14285714285 -> 6
    """
    # digits = (Decimal(1) / Decimal(denominator)).as_tuple().digits
    raise NotImplementedError("actual algorithm")  # TODO: implement this
    next_divisor = Decimal(1)
    dividend = Decimal(denominator)
    seen_divisors: list[Decimal] = []
    while True:
        print(seen_divisors)
        if next_divisor == Decimal(0):
            return len(seen_divisors)
        if next_divisor in seen_divisors:
            return len(seen_divisors[seen_divisors.index(next_divisor) - 1 :])
        seen_divisors.append(next_divisor)
        next_divisor = (dividend % next_divisor) * 10


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
