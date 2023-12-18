import re

red = re.compile(r"(\d+) red")
green = re.compile(r"(\d+) green")
blue = re.compile(r"(\d+) blue")


def part_two(doc):
    """
    Given a list of Games, determine the fewest amount of cubes needed to play each game

    For example:\n
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green (4R, 2G, 6B)

    Return the total of the powers of each game (r * g * b)
    """

    powers = []
    for game in doc:
        r = max([int(count) for count in red.findall(game)])
        g = max([int(count) for count in green.findall(game)])
        b = max([int(count) for count in blue.findall(game)])

        powers.append(r * g * b)

    return sum(powers)
