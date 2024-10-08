#!/usr/bin/env python3

# https://projecteuler.net/problem=29

def get_distinct_powers_count(upper_bound: int) -> int:
    """
    Return the amount of distinct powers a^b for
    2 <= a <= upper_bound and 2 <= b <= upper_bound

    Example: f(5) -> (4, 8, 9, 16, 25, 27, 32, 64,
    81, 125, 243, 256, 625, 1024, 3125) -> 15
    """
    seen: set[int] = set()
    for a in range(2, upper_bound + 1):
        for b in range(2, upper_bound + 1):
            seen.add(a**b)
    return len(seen)


print(get_distinct_powers_count(5))
print(get_distinct_powers_count(100))
