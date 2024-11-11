#!/usr/bin/env python3

# https://projecteuler.net/problem=18

from itertools import islice, pairwise


def maximum_path_sum(triangle: list[str]) -> int:
    """
    Return the greatest sum of elements that traverses from the top
    to the bottom of a triangle formed by a list of space-separated
    integers
    """
    total = int(triangle[0])
    current_position = 0
    for line, next_line in pairwise(triangle[1:]):
        left, right = tuple(
            islice(
                map(int, line.split()),
                current_position,
                current_position + 2,
            )
        )
        bottom_left, bottom_center, bottom_right = tuple(
            islice(
                map(int, next_line.split()),
                current_position,
                current_position + 3,
            )
        )
        left_path = left + max(bottom_center, bottom_left)
        right_path = right + max(bottom_right, bottom_center)
        chosen = {
            left_path: left,
            right_path: right,
        }[max(left_path, right_path)]
        total += chosen
        if chosen == right:
            current_position += 1
        continue
    return total + max(
        islice(
            map(int, triangle[-1].split()),
            current_position,
            current_position + 2,
        )
    )


print(
    maximum_path_sum(
        [
            "3",
            "7 4",
            "2 4 6",
            "8 5 9 3",
        ]
    )
)
print(
    maximum_path_sum(
        [
            "75",
            "95 64",
            "17 47 82",
            "18 35 87 10",
            "20 04 82 47 65",
            "19 01 23 75 03 34",
            "88 02 77 73 07 63 67",
            "99 65 04 28 06 16 70 92",
            "41 41 26 56 83 40 80 70 33",
            "41 48 72 33 47 32 37 16 94 29",
            "53 71 44 65 25 43 91 52 97 51 14",
            "70 11 33 28 77 73 17 78 39 68 17 57",
            "91 71 52 38 17 14 91 43 58 50 27 29 48",
            "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
            "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23",
        ]
    )
)
# with open("0067_triangle.txt") as big_triangle:
#     print(maximum_path_sum(big_triangle.readlines()))
