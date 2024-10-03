#!/usr/bin/env python3

# https://projecteuler.net/problem=20


def factorial(num: int) -> int:
    """Return the factorial of `num`"""
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


def sum_of_digits_in_factorial(num: int) -> int:
    """
    Return the sum of the digits of `num`!

    Example: f(10) -> 10! -> 3628800 -> -> 27
    """
    total = 0
    for i in str(factorial(num)):
        total += int(i)
    return total


print(sum_of_digits_in_factorial(10))
print(sum_of_digits_in_factorial(100))
