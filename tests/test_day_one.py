from textwrap import dedent

from aoc.day_one.part_one import part_one
from aoc.day_one.part_two import part_two


def test_part_one():
    ex = (
        dedent(
            """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
        )
        .strip("\n")
        .split("\n")
    )

    assert part_one(ex) == 142


def test_part_two():
    ex = (
        dedent(
            """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """
        )
        .strip("\n")
        .split("\n")
    )

    assert part_two(ex) == 281
