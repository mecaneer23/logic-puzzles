#!/usr/bin/env python3

# https://projecteuler.net/problem=15

import math


def get_route_amount(grid_size: int) -> int:
    """
    Return the amount of paths through a `grid_size` x `grid_size`
    grid, staying on edges and potentially turning at vertices
    going from the top left corner to the bottom right corner

    Example: f(2) -> 6
    """
    return math.comb(2 * grid_size, grid_size)


print(get_route_amount(2))
print(get_route_amount(20))
