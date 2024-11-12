#!/usr/bin/env python3

# https://codegolf.stackexchange.com/questions/59625/type-uniqchars


def test(obj1: object, obj2: object) -> None:
    """Test a"""
    if obj1 != obj2:
        print(f"{obj1} != {obj2}")


def remove_duplicates(string: str) -> str:
    """Remove duplicates from a string"""
    out = ""
    for char in string:
        if char not in out:
            out += char
    return out


test(remove_duplicates("Type unique chars!"), "Type uniqchars!")
test(
    remove_duplicates('"I think it\'s dark and it looks like rain", you said'),
    "\"I think'sdarloe,yu",
)
test(remove_duplicates("3.1415926535897932384626433832795"), "3.14592687")
