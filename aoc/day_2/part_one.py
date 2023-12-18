import re

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

red = re.compile(r"(\d+) red")
green = re.compile(r"(\d+) green")
blue = re.compile(r"(\d+) blue")


def part_one(doc):
    """
    Given a list of Games, determine which are possible outcomes given a max number
    of available red, green and blues cubes.

    For example:\n
    With a maximum of 12R, 14G and 14B Cubes\n
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green - possible (5R, 4G, 9B)\n
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red - not

    Return the sum of the ids of all possible games
    """

    total = 0
    for index, game in enumerate(doc, start=1):
        r = list(
            filter(
                lambda x: x > MAX_RED_CUBES, [int(count) for count in red.findall(game)]
            )
        )
        g = list(
            filter(
                lambda x: x > MAX_GREEN_CUBES,
                [int(count) for count in green.findall(game)],
            )
        )
        b = list(
            filter(
                lambda x: x > MAX_BLUE_CUBES,
                [int(count) for count in blue.findall(game)],
            )
        )

        if len(r) == 0 and len(g) == 0 and len(b) == 0:
            total += index

    return total
