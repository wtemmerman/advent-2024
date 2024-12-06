import os
from collections import Counter

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)


def get_list(reader: FileInputReader, need_to_be_order: bool = True) -> tuple[list, list]:
    print(f"Reading file {reader.file_path} line by line:")
    left_list = []
    right_list = []
    for line in reader.read_line_by_line():
        # print(line.split('   '))
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    if need_to_be_order:
        left_list.sort()
        right_list.sort()

    return left_list, right_list


def calculate_diff(reader: FileInputReader) -> int:
    left_list, right_list = get_list(reader)

    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

    print(total_distance)
    return total_distance


def calculate_similarity(reader: FileInputReader) -> int:
    left_list, right_list = get_list(reader, need_to_be_order=False)

    total_similarity = 0
    counter_right_similarity = Counter(right_list)
    # print(counter_right_similarity)
    for left_element in left_list:
        # print(f'LE {left_element}')
        total_similarity += left_element * counter_right_similarity[left_element]
        # print(f'TMP TS {total_similarity}')

    print(total_similarity)
    return total_similarity


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert calculate_diff(reader_test) == 11
    assert calculate_diff(reader) == 1197984


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert calculate_similarity(reader_test) == 31
    assert calculate_similarity(reader) == 23387399


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
