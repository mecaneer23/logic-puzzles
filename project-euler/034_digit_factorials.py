#!/usr/bin/env python3

# https://projecteuler.net/problem=34

from functools import cache


@cache
def factorial(num: int) -> int:
    """Return the factorial of `num`"""
    if num <= 1:
        return num
    return num * factorial(num - 1)


def get_digit_factorials() -> int:
    """
    Return the sum of all numbers equal to the sum of the factorial of their digits
    """
    total = 0
    counter = 3
    while True:
        digit_factorial_sum = sum(map(factorial, map(int, str(counter))))
        if digit_factorial_sum == counter:
            total += counter
        counter += 1
        # TODO: arbitrary stopping point; how can we detect the true end?
        if counter > 1_000_000:
            return total


print(get_digit_factorials())
