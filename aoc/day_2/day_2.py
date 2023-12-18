from part_one import part_one
from part_two import part_two


def day_two():
    with open("input.txt") as file:
        lines = file.readlines()
        print(f"Day two, part one: {part_one(lines)}")
        print(f"Day two, part two: {part_two(lines)}")


day_two()
