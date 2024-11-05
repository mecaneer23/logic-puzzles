#!/usr/bin/env python3

# https://projecteuler.net/problem=056

def get_largest_digit_sum() -> int:
    """
    Considering natural numbers of the form,
    a^b, where a,b < 100, what is the maximum
    sum of digits?
    """
    largest = 0
    for i in range(100):
        for j in range(100):
            largest = max(largest, sum(int(i) for i in str(i**j)))
    return largest

print(get_largest_digit_sum())
