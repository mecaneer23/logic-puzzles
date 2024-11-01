#!/usr/bin/env python3

# https://projecteuler.net/problem=12

from math import sqrt


def get_num_factors(num: int) -> int:
    """
    Returns the number of factors a given number
    has, including 1 and itself
    """
    factors = 0
    for possible_factor in range(1, int(sqrt(num)) + 1):
        if num % possible_factor == 0:
            factors += 1
            if possible_factor != num // possible_factor:
                factors += 1
    return factors


def get_highly_divisible_triangle_number(amount_of_divisors: int) -> int:
    """
    Returns the first triangle number to have over
    `amount_of_divisors` divisors

    Example: f(5) -> 28
    """
    counter = 1
    triangle_number = counter

    while True:
        if get_num_factors(triangle_number) > amount_of_divisors:
            return triangle_number
        counter += 1
        triangle_number += counter


print(get_highly_divisible_triangle_number(5))
print(get_highly_divisible_triangle_number(500))
