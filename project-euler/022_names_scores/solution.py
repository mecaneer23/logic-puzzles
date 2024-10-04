#!/usr/bin/env python3

# https://projecteuler.net/problem=22


def get_name_score() -> int:
    """
    Read the names file, return the sum of name scores.

    A name score is the product of the position of the
    name in the sorted list and the sum of its characters
    (A = 1, B = 2, etc.)
    """
    with open("names.txt", "r", encoding="utf-8") as file:
        names = sorted(file.read().replace('"', "").split(","))

    name_score = 0
    for index, name in enumerate(names, start=1):
        letter_total = 0
        for character in name:
            letter_total += ord(character) - 64
        name_score += letter_total * index
    return name_score


print(get_name_score())
