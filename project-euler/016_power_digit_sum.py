#!/usr/bin/env python3

# https://projecteuler.net/problem=16

def get_power_digit_sum(power: int) -> int:
    """
    Return the sum of the digits of 2^`power`

    Example: f(15) -> 2^15 -> 32768 -> (3, 2, 7, 6, 8) -> 26
    """
    total = 0
    for i in str(2**power):
        total += int(i)
    return total


print(get_power_digit_sum(15))
print(get_power_digit_sum(1000))
