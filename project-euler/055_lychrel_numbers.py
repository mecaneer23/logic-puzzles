#!/usr/bin/env python3

# https://projecteuler.net/problem=55


def is_palindrome(num: int) -> bool:
    """
    Returns whether the given number is a palindrome
    using string conversion.

    Borrowed from #004
    """
    str_num = str(num)
    return str_num == str_num[::-1]


def is_lychrel_number(num: int) -> bool:
    """
    Return whether `num` will never produce a palindrome
    when recursively added to its reverse
    """
    max_iterations = 50
    base_num = num
    for _ in range(max_iterations):
        base_num += int(str(base_num)[::-1])
        if is_palindrome(base_num):
            return False
    return True


def get_lychrel_numbers() -> int:
    """
    Return the amount of Lychrel numbers below 10_000
    """
    return sum(1 for n in range(10_000) if is_lychrel_number(n))


print(get_lychrel_numbers())
