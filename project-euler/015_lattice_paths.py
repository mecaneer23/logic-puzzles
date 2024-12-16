#!/usr/bin/env python3

# https://projecteuler.net/problem=15


def remove_top_right_vertice(
    current_vertices: list[tuple[int, int]], grid_size: int
) -> list[tuple[int, int]]:
    """Remove the top right most vertice from a list of points"""
    for i in range(grid_size + 1):
        for j in range(grid_size, -1, -1):
            if (i, j) in current_vertices and (i, j) not in {
                (0, 0),
                (grid_size, grid_size),
            }:
                current_vertices.remove((i, j))
                return current_vertices
    raise ValueError("No more points to remove")


def get_route_amount(grid_size: int) -> int:
    """
    Return the amount of paths through a `grid_size` x `grid_size`
    grid, staying on edges and potentially turning at vertices
    going from the top left corner to the bottom right corner

    Example: f(2) -> 6
    """
    found_routes = 0
    current_vertices = [
        (i, j) for i in range(grid_size + 1) for j in range(grid_size + 1)
    ]
    print(current_vertices)
    current_x = 0
    current_y = 0
    route_length = -1
    while True:
        print(current_x, current_y)
        if (current_x, current_y) in current_vertices:
            current_x += 1
        else:
            current_x -= 1
            print(current_x, current_y)
        route_length += 1
        if route_length > grid_size**2 + 1:
            return found_routes
        if (current_x, current_y) == (grid_size, grid_size):
            route_length = 0
            found_routes += 1
            current_x = 0
            current_y = 0
            current_vertices = remove_top_right_vertice(
                current_vertices,
                grid_size,
            )
            print(current_vertices)


print(get_route_amount(2))
# print(get_route_amount(20))
