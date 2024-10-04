#!/usr/bin/env python3

# https://projecteuler.net/problem=25

def get_first_n_digit_fibonacci_number_index(n: int) -> int:
    """
    Return the index of the first `n` digit Fibonnaci number

    Example: f(3) -> 144 -> 12
    """
    a = 1
    b = 1
    counter = 2
    while True:
        a += b
        counter += 1
        if len(str(a)) == n:
            return counter
        b += a
        counter += 1
        if len(str(b)) == n:
            return counter


print(get_first_n_digit_fibonacci_number_index(3))
print(get_first_n_digit_fibonacci_number_index(1000))
