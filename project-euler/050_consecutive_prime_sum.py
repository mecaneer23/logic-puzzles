#!/usr/bin/env python3

# https://projecteuler.net/problem=50

from functools import cache
from math import sqrt


@cache
def is_prime(num: int) -> bool:
    """Returns whether a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_below(upper_bound: int) -> list[int]:
    """
    Return an ordered list of primes below an upper bound
    """
    primes: list[int] = []
    for i in range(upper_bound):
        if is_prime(i):
            primes.append(i)
    return primes


def get_longest_consecutive_prime_sum_below(upper_bound: int) -> int:
    """
    Return the prime sum with the greatest amount of consecutive
    prime elements below a given `upper_bound`

    Examples:
        f(100) -> (2, 3, 5, 7, 11, 13) -> 41
        f(1000) -> 21 terms -> 953
    """
    width = 1
    primes = get_primes_below(upper_bound)
    # increase width until current_sum > upper_bound
    while True:
        if sum(primes[:width]) >= upper_bound:
            width -= 1
            break
        width += 1
    primes = primes[:width]
    while True:
        # check all groups of current width
        for start in range(len(primes) - width, -1, -1):
            current_sum = sum(primes[start : start + width])
            if is_prime(current_sum):
                return current_sum
        width -= 1


def attempt_3(upper_bound: int) -> int:
    primes = get_primes_below(upper_bound)
    prime_count = len(primes)
    max_sum = 0
    max_length = 0
    for start in range(prime_count):
        for width in range(prime_count, 0, -1):
            current_sum = sum(primes[start : start + width])
            if current_sum >= upper_bound:
                continue
            if is_prime(current_sum):
                max_sum = current_sum
                max_length = width
    return max_sum, max_length


def attempt_2(upper_bound: int) -> int:
    start = 0
    width = 1
    primes = get_primes_below(upper_bound)
    max_sum = 0
    max_width = 0
    for _ in range(upper_bound):
        current_sum = sum(primes[start : start + width])
        if current_sum >= upper_bound:
            start += 1
        if is_prime(current_sum):
            max_sum = current_sum
            max_width = width
        width += 1
    return max_sum

    # if is_prime(current_sum) and current_sum > max_sum:
    #     max_sum = current_sum


def attempt_1(upper_bound: int) -> int:
    """
    Return the largest sum of consecutive primes which remains prime
    below a given `upper_bound`

    Doesn't work:
        calculates consecutive primes starting at the 0th prime,
        rather than using a sliding window approach

    Examples:
        f(100) -> (2, 3, 5, 7, 11, 13) -> 41
        f(1000) -> 21 terms -> 953
    """
    prime_sum = 0
    max_sum = 0
    for i in range(upper_bound):
        if is_prime(i):
            prime_sum += i
        if prime_sum > upper_bound:
            return max_sum
        if is_prime(prime_sum) and prime_sum > max_sum:
            max_sum = prime_sum
    return 0


print(get_longest_consecutive_prime_sum_below(100))
print(get_longest_consecutive_prime_sum_below(1000))
print(get_longest_consecutive_prime_sum_below(1_000_000))
