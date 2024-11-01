#!/usr/bin/env python3

# https://projecteuler.net/problem=42


from math import sqrt


def is_triangle_number(num: int) -> bool:
    """
    Return whether a given number is
    a triangle number
    """
    return (-(1 - sqrt(1 + 8 * num)) / 2).is_integer()


def get_coded_triangle_word_amount() -> int:
    """
    Return the amount of words in `words.txt`
    which are coded triangle numbers
    """
    total = 0
    with open("words.txt", "r", encoding="utf-8") as file:
        words = file.read().replace('"', "").split(",")
    for word in words:
        word_value = sum(ord(letter) - 64 for letter in word)
        if is_triangle_number(word_value):
            total += 1
    return total


print(get_coded_triangle_word_amount())
