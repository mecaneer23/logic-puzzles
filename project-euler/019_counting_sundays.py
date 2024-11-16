#!/usr/bin/env python3

# https://projecteuler.net/problem=019


def count_sundays() -> int:
    """
    Return the amount of Sundays that fell on the
    first of the month during the 20th century
    """
    days_per_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    month = 1
    day = 1
    year = 1901
    weekday = 2  # weekday = int[1-7], where 1 = Sunday
    sundays = 0
    while year < 2001:
        if weekday == 8:
            weekday = 1
            if day == 1:
                sundays += 1
        if day == days_per_month[month]:
            month += 1
            day = 0
        if month == 13:
            month = 1
            year += 1
            days_per_month[2] = (
                29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
            )
        day += 1
        weekday += 1
    return sundays - 1  # remove Jan 1 2001


print(count_sundays())
