#!/usr/bin/env python3

# https://codegolf.stackexchange.com/questions/276081/your-average-character


def average_char(string: str) -> str:
    """
    Return the average character of a string by
    converting characters to numerical representations,
    finding an average (to the nearest integer), and
    converting the average back to a character.
    """
    lowercase_offset = 96
    char_sum = 0
    length = 0
    for char in string.lower():
        if char.isalpha():
            length += 1
            char_sum += ord(char) - lowercase_offset
    return chr(round(char_sum / length) + lowercase_offset)


# average_char = lambda s:chr(round(sum(ord(c)-96 for c in s.lower()if c.isalpha())/sum(c.isalpha()for c in s))+96)


assert average_char("a") == "a", average_char("a")
assert average_char("aaaaa") == "a"
assert average_char("abcde") == "c"
assert average_char("bcde") == "d"
assert average_char("a1!b2@c") == "b", average_char("a1!b2@c")
assert average_char("ABCde") == "c"
assert average_char("POP") == "p"
assert average_char("A B C") == "b"

try:
    average_char("@@@@")
    print("Test case failed: @@@@")
except ZeroDivisionError:
    pass

try:
    average_char("")
    print('Test case failed: ""')
except ZeroDivisionError:
    pass
