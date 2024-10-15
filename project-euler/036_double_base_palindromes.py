#!/usr/bin/env python3

# https://projecteuler.net/problem=36


def get_double_base_palindrome_sum() -> int:
    """
    Return the sum of all numbers less than 1_000_000
    that are palindromic in both base 10 and base 2
    """
    total = 0
    for num in range(1, 1_000_000):
        str_num = str(num)
        bin_num = bin(num)[2:]
        if str_num == str_num[::-1] and bin_num == bin_num[::-1]:
            total += num
    return total


print(get_double_base_palindrome_sum())
