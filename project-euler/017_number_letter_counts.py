#!/usr/bin/env python3

# https://projecteuler.net/problem=017


def get_spelling(num: int) -> str:
    """
    Return the spelling of a number (1-1000) using British standards
    """
    table = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "15": "fifteen",
        "18": "eighteen",
        "20": "twenty",
        "30": "thirty",
        "40": "forty",
        "50": "fifty",
        "60": "sixty",
        "70": "seventy",
        "80": "eighty",
        "90": "ninety",
        "1000": "onethousand",
    }
    str_num = str(num)
    if str_num in table:
        return table[str_num]
    if len(str_num) == 2:
        if str_num[0] == "1":
            return f"{table[str_num[1]]}teen"
        return f"{table[str_num[0] + '0']}{table[str_num[1]]}"
    triple_digit_output = f"{table[str_num[0]]}hundred"
    if str_num[1:] != "00":
        triple_digit_output += f"and{get_spelling(int(str_num[1:]))}"
    return triple_digit_output


def get_number_letter_counts() -> int:
    """
    Return the sum of letters in all of the spelled out numbers 1-1000
    """
    return sum(map(len, (get_spelling(i) for i in range(1, 1001))))


print(get_number_letter_counts())
