import re
from functools import reduce

word_number_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_value(line):
    """
    Return a new string comprised of the first and last digit found within a given
    string argument.

    Digits may appear as a number or a word, words are converted to their numerical
    format.

    "j4m3s" -> "43"\n
    "treb7uchetone" -> "71"\n
    "eightwothree" -> "83"
    """
    string_values = re.findall(
        r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line
    )
    values = [
        val if len(val) == 1 else word_number_to_digit[val] for val in string_values
    ]
    return int(values[0] + values[-1])


def part_two(doc):
    """
    With a document made up of multiple lines, get the calibration value for each and
    return the sum of all calibration values
    """
    return reduce((lambda x, y: x + get_calibration_value(y)), doc, 0)
