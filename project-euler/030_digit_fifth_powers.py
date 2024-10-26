#!/usr/bin/env python3

# https://projecteuler.net/problem=30

from functools import cache


def get_number_digit_powers(power: int) -> int:
    """
    Return the sum of the numbers that can be
    written as the sum of the `power`th power
    of their digits

    Example: f(4) -> (1634, 8208, 9474) -> 19316
    """

    @cache
    def get_digit_power(digit: str) -> int:
        """Return a digit raised to a given power"""
        return int(digit) ** power

    total = 0
    test_number = 1
    while True:
        test_number += 1
        digit_power_sum = sum(map(get_digit_power, str(test_number)))
        if digit_power_sum == test_number:
            total += test_number
            print(total)
            continue
        # TODO: add if statement to break rather than just printing increases
    return total


# print(get_number_digit_powers(4))
print(get_number_digit_powers(5))
