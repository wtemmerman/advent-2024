import os

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)


def is_safe(elements: list[int]) -> bool:
    decrease = True if elements[0] > elements[1] else False

    for i in range(len(elements) - 1):
        current, next_element = elements[i], elements[i + 1]
        if decrease and (current <= next_element or abs(current - next_element) > 3):
            return False
        if not decrease and (current >= next_element or abs(current - next_element) > 3):
            return False

    return True


def is_safe_with_dampener(elements: list[int]) -> bool:
    for i in range(len(elements)):
        modified_elements = elements[:i] + elements[i + 1 :]
        if is_safe(modified_elements):
            return True
    return False


def found_safe_report(reader: FileInputReader) -> int:
    print(f"Reading file {reader.file_path} line by line:")
    safe_count = 0
    for line in reader.read_line_by_line():
        elements = list(map(int, line.split()))
        if elements[0] == elements[1]:
            continue

        if is_safe(elements):
            safe_count += 1
    print(safe_count)
    return safe_count


def found_safe_report_with_dampener(reader: FileInputReader) -> int:
    print(f"Reading file {reader.file_path} line by line:")
    safe_count = 0

    for line in reader.read_line_by_line():
        elements = list(map(int, line.split()))

        if is_safe(elements) or is_safe_with_dampener(elements):
            safe_count += 1
    print(safe_count)
    return safe_count


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert found_safe_report(reader_test) == 2
    assert found_safe_report(reader) == 369


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert found_safe_report_with_dampener(reader_test) == 4
    assert found_safe_report_with_dampener(reader) == 428


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
