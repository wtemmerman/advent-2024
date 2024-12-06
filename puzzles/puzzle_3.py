import os
import re

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)


def add_mul(reader: FileInputReader):
    print(f"Reading file {reader.file_path}:")
    corrupted_memory = "".join(reader.read_all_lines())

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, corrupted_memory)
    total = 0
    for x, y in matches:
        product = int(x) * int(y)
        total += product
        # print(f"Valid instruction: mul({x},{y}) = {product}")

    print(f"Total sum: {total}")


def sum_enabled_mul_instructions(reader: FileInputReader):
    print(f"Reading file {reader.file_path}:")
    corrupted_memory = "".join(reader.read_all_lines())

    mul_regex = r"mul\((\d+),(\d+)\)"
    control_regex = r"do\(\)|don't\(\)"

    mul_enabled = True
    total_sum = 0

    for match in re.finditer(f"{mul_regex}|{control_regex}", corrupted_memory):
        # print(match)
        if match.group(0).startswith("mul"):
            # Handle mul(X, Y) instructions
            if mul_enabled:
                x, y = map(int, match.groups()[:2])
                total_sum += x * y
        elif match.group(0) == "do()":
            # Enable future mul instructions
            mul_enabled = True
        elif match.group(0) == "don't()":
            # Disable future mul instructions
            mul_enabled = False

    print(f"Total sum: {total_sum}")


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    add_mul(reader_test)
    add_mul(reader)


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    sum_enabled_mul_instructions(reader_test)
    sum_enabled_mul_instructions(reader)


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
