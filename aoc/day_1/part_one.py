import re
from functools import reduce


def get_calibration_value(line):
    """
    Return a new string comprised of the first and last digit found within a given
    string argument

    "j4m3s" -> "43"\n
    "treb7uchet" -> "77"
    """
    ints = re.findall(r"\d", line)
    return int(ints[0] + ints[-1])


def part_one(doc):
    """
    With a document made up of multiple lines, get the calibration value for each and
    return the sum of all calibration values
    """
    return reduce((lambda x, y: x + get_calibration_value(y)), doc, 0)
