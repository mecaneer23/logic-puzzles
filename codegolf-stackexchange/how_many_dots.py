#!/usr/bin/env python3

# https://codegolf.stackexchange.com/questions/276019/how-many-dots-are-there


def dot_count(string: str) -> int:
    """
    Return the amount of dots in `string`.

    Dots are found in the characters `i j . ; ! ?` and `:`
    """
    return attempt_2(string)


def attempt_1(string: str) -> int:
    """Simplest iterative solution"""
    count = 0
    for i in string:
        if i in "ij.;!?":
            count += 1
            continue
        if i == ":":
            count += 2
    return count


def attempt_2(string: str) -> int:
    """Use string.count"""
    return sum(map(string.count, "ij.;!?::"))


assert dot_count("Sphinx of black quartz, judge my vow!") == 3
assert dot_count("Lorem ipsum: dolor sit amet?") == 5
assert dot_count("Programming Puzzles & Code Golf") == 1
assert dot_count("ij.;!?:") == 8
assert dot_count("pericardiomediastinitis") == 6
assert dot_count("formaldehydesulphoxylate") == 0
assert dot_count("") == 0
