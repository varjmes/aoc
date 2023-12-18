#!/usr/bin/python3
# With thanks: https://github.com/jonathanpaulson/AdventOfCode/blob/master/get_input.py

# poetry run python ./setup_day.py --year {year} --day {day}
import argparse
import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SESSION = os.getenv("SESSION")

useragent = "https://git.jmes.tech/james/aoc/blob/main/get_input.py by james"
parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("--year", type=int, default=2023)
parser.add_argument("--day", type=int, default=1)
args = parser.parse_args()

cmd = f"curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie \"session={SESSION}\" -A '{useragent}'"
print(f"🚀 Fetching input.txt for Year {args.year}, Day {args.day}")
output = subprocess.check_output(cmd, shell=True)  # noqa: S602
output = output.decode("utf-8").strip("\n")

print("🚀 Setting up the days files")
Path(f"{Path.cwd()}/day_{args.day}").mkdir()
Path(f"{Path.cwd()}/day_{args.day}/day_{args.day}.py").touch()
Path(f"{Path.cwd()}/day_{args.day}/part_one.py").touch()
Path(f"{Path.cwd()}/day_{args.day}/part_two.py").touch()
Path(f"../tests/test_day_{args.day}.py").touch()

with open(f"{Path.cwd()}/day_{args.day}/input.txt", "w") as file:
    file.write(output)
