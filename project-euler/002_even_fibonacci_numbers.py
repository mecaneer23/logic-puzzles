#!/usr/bin/env python3
# https://projecteuler.net/problem=2

def even_fib_sum() -> int:
    """
    Returns sum of even fibonacci numbers less than 4,000,000

    Uses {1, 2} as the initial values
    """
    max_value = 4_000_000
    value_a = 1
    value_b = 2
    even_sum = value_b

    while True:
        value_a += value_b
        if value_a > max_value:
            break
        if value_a % 2 == 0:
            even_sum += value_a

        value_b += value_a
        if value_b > max_value:
            break
        if value_b % 2 == 0:
            even_sum += value_b

    return even_sum


print(even_fib_sum())
