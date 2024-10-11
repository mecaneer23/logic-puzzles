#!/usr/bin/env python3

# https://projecteuler.net/problem=30

def get_number_digit_powers(power: int) -> int:
    """
    Return the sum of the numbers that can be
    written as the sum of the `power`th power
    of their digits

    Example: f(4) -> (1634, 8208, 9474) -> 19316
    """
    total = 0
    test_number = 1
    while True:
        test_number += 1
        digit_power_sum = sum(map(lambda x: pow(int(x), power), str(test_number)))
        if digit_power_sum == test_number:
            total += test_number
            continue
        if power == 5 and test_number > 194979:  # TODO: how do we know this is the last valid number?
            break
    return total


print(get_number_digit_powers(4))
print(get_number_digit_powers(5))