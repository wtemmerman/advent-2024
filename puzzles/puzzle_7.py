import os
from itertools import product

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)


def evaluate_expression(numbers, ops):
    result = numbers[0]

    for op, num in zip(ops, numbers[1:]):
        if op == "+":
            result = result + num
        elif op == "*":
            result = result * num
        elif op == "||":
            result = int(str(result) + str(num))
    return result


def can_achieve_target(target: int, numbers: list[int], v2: bool = False) -> bool:
    if len(numbers) == 1:
        return target == numbers[0]

    length = len(numbers) - 1
    elements = ["+", "*"] if not v2 else ["+", "*", "||"]
    for ops in product(elements, repeat=length):
        val = evaluate_expression(numbers, ops)
        if val == target:
            return True
    return False


def total_calibration(reader: FileInputReader, v2: bool = False) -> int:
    total = 0
    for line in reader.read_line_by_line():
        target_str, nums_str = line.split(":")
        target = int(target_str.strip())
        numbers = list(map(int, nums_str.strip().split()))

        # Check if we can achieve the target
        if can_achieve_target(target, numbers, v2):
            total += target

    print(f"Total calibration: {total}")
    return total


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert total_calibration(reader_test) == 3749
    assert total_calibration(reader) == 850435817339


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert total_calibration(reader_test, v2=True) == 11387
    assert total_calibration(reader, v2=True) == 104824810233437


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
