from part_one import part_one
from part_two import part_two


def day_one():
    with open("input.txt") as file:
        lines = file.readlines()
        print(f"Day one, part one: {part_one(lines)}")
        print(f"Day one, part two: {part_two(lines)}")


day_one()
