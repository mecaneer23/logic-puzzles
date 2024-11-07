#!/usr/bin/env python3

# https://projecteuler.net/problem=59

from itertools import cycle
from string import ascii_lowercase
from typing import Iterable


def decode(cipher: Iterable[int], key: str) -> str:
    """
    Use a repeated key to decode a cipher
    """
    decoded_cipher = ""
    for k, v in zip(cycle(map(ord, key)), cipher):
        decoded_cipher += chr(k ^ v)
    return decoded_cipher


def decrypt_cipher(substring_likely_in_cipher: str) -> str:
    """
    Decrypt a cipher stored in "0059_cipher.txt"
    """
    with open("0059_cipher.txt", "r", encoding="utf-8") as file:
        cipher = list(map(int, file.read().split(",")))
    for letter_1 in ascii_lowercase:
        for letter_2 in ascii_lowercase:
            for letter_3 in ascii_lowercase:
                key = f"{letter_1}{letter_2}{letter_3}"
                decoded_string = decode(cipher, key)
                if (
                    substring_likely_in_cipher in decoded_string
                ):  # TODO: won't work for all strings
                    return decoded_string
    raise ValueError


def string_to_ascii_sum(string: str) -> int:
    """
    Return the sum of the ascii-ified characters in a string
    """
    return sum(map(ord, string))


print(string_to_ascii_sum(decrypt_cipher(" and ")))
