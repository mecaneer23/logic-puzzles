#!/usr/bin/env python3

# https://projecteuler.net/problem=14


def get_collatz_sequence_length_staring_with(num: int) -> int:
    """
    Return the length of the collatz sequence starting with `num`

    Example: f(13) -> (13, 40, 20, 10, 5, 16, 8, 4, 2, 1) -> 10
    """
    current = num
    length = 0
    while True:
        length += 1
        if current == 1:
            return length
        if current % 2 == 0:
            current //= 2
            continue
        current = current * 3 + 1


def get_longest_collatz_sequence(num: int) -> int:
    """
    Return the longest Collatz sequence under a given number
    """
    max_sequence_length = 0
    max_start_value = 0

    for i in range(1, num + 1):
        current_length = get_collatz_sequence_length_staring_with(i)
        if current_length > max_sequence_length:
            max_sequence_length = current_length
            max_start_value = i
    return max_start_value


print(get_longest_collatz_sequence(1_000_000))
