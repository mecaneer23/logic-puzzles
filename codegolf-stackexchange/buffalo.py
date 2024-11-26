#!/usr/bin/env python3

# https://codegolf.stackexchange.com/questions/218284/output-buffalo-buffalo-buffalo-buffalo-buffalo-buffalo-buffalo-buffalo


def buffalos() -> None:
    """
    Print \"Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo\"
    """
    print(*(b + "uffalo" for b in "BbBbbbBb"))


if __name__ == "__main__":
    buffalos()
