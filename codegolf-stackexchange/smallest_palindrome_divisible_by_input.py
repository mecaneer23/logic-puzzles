#!/usr/bin/env python3

# https://codegolf.stackexchange.com/questions/91023/smallest-palindrome-divisible-by-the-input


def get_palindrome(n: int) -> int:
    """Return the smallest palindrome divisible by n"""
    counter = n
    while True:
        if counter % n == 0 and int(str(counter)[::-1]) == counter:
            return counter
        counter += 1


assert get_palindrome(1) == 1
assert get_palindrome(2) == 2
assert get_palindrome(16) == 272
assert get_palindrome(17) == 272
assert get_palindrome(42) == 252
assert get_palindrome(111) == 111
assert get_palindrome(302) == 87278
assert get_palindrome(1234) == 28382
