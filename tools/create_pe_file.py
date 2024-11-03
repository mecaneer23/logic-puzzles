#!/usr/bin/env python3

"""
Create a new project euler file based on an input number
"""

from argparse import ArgumentParser
from requests import get


def get_args() -> str:
    parser = ArgumentParser("Create Project Euler File")
    parser.add_argument("number")
    return parser.parse_args().number


def parse_csv_for_title(problem_id: str) -> str:
    """Call projecteuler api to get title for a given `problem_id`"""
    reader = iter(
        get("https://projecteuler.net/minimal=problems;csv").text.splitlines()
    )
    headers = next(reader).replace('"', "").split(",")
    for line in reader:
        line = dict(zip(headers, line.split(",")))
        if line["ID"] == problem_id.lstrip("0"):
            return line["Title"].replace('"', "").lower().replace(" ", "_")
    raise ValueError("Invalid `problem_id`")


def create_file(problem_id: str) -> None:
    """Create new file"""
    title = parse_csv_for_title(problem_id)
    with open(f"{problem_id.zfill(3)}_{title}.py", "w", encoding="utf-8") as file:
        file.write(
            "#!/usr/bin/env python3\n\n"
            f"# https://projecteuler.net/problem={problem_id}\n"
        )
    print("File successfully created")


if __name__ == "__main__":
    create_file(get_args())
