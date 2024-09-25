#!/usr/bin/env python3

# https://projecteuler.net/problem=4

def is_palindrome(num: int) -> bool:
    """
    Returns whether the given number is a palindrome
    using string conversion.

    My understanding is for large numbers, converting
    to a string is faster (and simpler) than looping
    over the digits of a number.
    """
    str_num = str(num)
    return str_num == str_num[::-1]


def largest_palindrome_product(digits: int) -> int:
    """
    Return the largest palindrome made from the product of two `digit`-long integers

    Example: f(2) -> (91, 99) -> 9009
    """
    for i in range(10**digits - 1, 10 ** (digits - 1), -1):
        for j in range(10**digits - 1, 10 ** (digits - 1), -1):
            product = i * j
            if is_palindrome(product):
                return product
    return 0


print(largest_palindrome_product(2))
print(largest_palindrome_product(3))
