#!/usr/bin/env python3

# https://projecteuler.net/problem=39


from math import sqrt


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    """
    Returns whether (a, b, c) is a valid Pythagorean triplet

    A valid Pythagorean triplet is a set of three natural numbers
    `a` < `b` < `c` for which `a`^2 + `b`^2 = `c`^2
    """
    return a < b < c and a**2 + b**2 == c**2


def get_num_solutions(perimeter: int) -> int:
    """
    Return the amount of solutions of
    `a`^2 + `b`^2 = `c`^2 where `a` + `b` + `c` = `perimeter`

    General function borrowed from #9
    """
    solutions = 0
    for c in range(perimeter // 2, 2, -1):
        for b in range(c - 1, 2, -1):
            possible_a = sqrt(c**2 - b**2)
            a = int(possible_a)
            if possible_a != a:
                continue
            if a > b:
                break
            if a + b + c == perimeter and is_pythagorean_triplet(a, b, c):
                solutions += 1
    return solutions


def maximize_solutions() -> int:
    """
    Return the perimeter (<=1000) of the right angle
    triangle which can be created in the most ways
    """
    max_perimeter = 0
    max_solutions = 0
    for perimeter in range(1001):
        solutions = get_num_solutions(perimeter)
        if solutions > max_solutions:
            max_solutions = solutions
            max_perimeter = perimeter
    return max_perimeter


print(maximize_solutions())
