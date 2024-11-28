#!/usr/bin/env python3

# https://projecteuler.net/problem=69


def get_totient_sieve(upper_bound: int) -> list[int]:
    """
    Computes the totient function for all
    numbers from 1 to `upper_bound`
    using a sieve method

    This method required significant research
    compared to the simpler gcf method (see
    git blame for this file)
    """
    totients: list[float] = list(range(upper_bound + 1))
    for possible_prime in range(2, upper_bound + 1):
        if totients[possible_prime] == possible_prime:
            for multiple in range(possible_prime, upper_bound + 1, possible_prime):
                totients[multiple] *= 1 - 1 / possible_prime
    return list(map(int, totients))


def get_max_n_over_totient_n(upper_bound: int) -> int:
    """
    Return n which maximizes n/totient(n) <= upper_bound

    Example: f(10) -> 3 -> 6
    """
    totient = get_totient_sieve(upper_bound)
    max_totient = 0
    max_n = 0
    for n in range(2, upper_bound + 1):
        totient_n = n / totient[n]
        if totient_n > max_totient:
            max_totient = totient_n
            max_n = n
    return max_n


print(get_max_n_over_totient_n(10))
print(get_max_n_over_totient_n(1_000_000))
