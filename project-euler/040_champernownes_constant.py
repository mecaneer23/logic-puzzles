#!/usr/bin/env python3

# https://projecteuler.net/problem=40


def get_pos_int_concat_str() -> str:
    """
    Return a string of length == 1_000_000 created
    from the concatenation of positive integers
    """
    result = "0"
    count = 1
    while True:
        if len(result) > 1_000_000:
            return result
        result += str(count)
        count += 1


def get_champernownes_constant() -> int:
    """Return Champernowne's Constant"""
    product = 1
    # TODO: shouldn't need to generate the whole string to determine 7 characters
    pos_int_str = get_pos_int_concat_str()
    for power in range(7):
        product *= int(pos_int_str[10 ** power])
    return product


print(get_champernownes_constant())
