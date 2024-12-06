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

    # Define regex pattern for valid mul(X,Y)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find all valid matches
    matches = re.findall(pattern, corrupted_memory)

    # Calculate the sum of the products
    total = 0
    for x, y in matches:
        product = int(x) * int(y)
        total += product
        # print(f"Valid instruction: mul({x},{y}) = {product}")

    print(f"Total sum: {total}")


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    add_mul(reader_test)
    add_mul(reader)


# def part2():
#     reader_test = FileInputReader(f"day_{number}_input_test.txt")
#     reader = FileInputReader(f"day_{number}_input.txt")


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    # part2()
