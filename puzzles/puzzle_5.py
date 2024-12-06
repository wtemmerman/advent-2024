import os

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)


def parse_input(input_text: str):
    """Parse the input text into ordering rules and updates."""
    rules_section, updates_section = input_text.strip().split("\n\n")

    # Parse rules
    rules = []
    for rule in rules_section.splitlines():
        x, y = map(int, rule.split("|"))
        rules.append((x, y))

    # Parse updates
    updates = [list(map(int, line.split(","))) for line in updates_section.splitlines()]

    return rules, updates


def validate_update(update, rules):
    """Validate an update against the given rules."""
    # Create a map of page indices for the current update
    page_index = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        # Ignore rules if x or y is not in the current update
        if x not in page_index or y not in page_index:
            continue
        # Validate the order
        if page_index[x] >= page_index[y]:
            return False

    return True


def find_middle_pages_sum(reader: FileInputReader, word="XMAS") -> int:
    print(f"Reading file {reader.file_path}:")
    entire_content = reader.get_entire_content()
    rules, updates = parse_input(entire_content)
    total_middle_sum = 0

    for update in updates:
        if validate_update(update, rules):
            # Calculate the middle page
            middle_page = update[len(update) // 2]
            total_middle_sum += middle_page

    print(f"Total middle sum {total_middle_sum}")
    return total_middle_sum


def is_update_correct(rules: list[tuple[int, int]], update: list[int]) -> bool:
    page_positions = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in page_positions and y in page_positions:
            if page_positions[x] > page_positions[y]:
                return False
    return True


def reorder_update(rules: list[tuple[int, int]], update: list[int]) -> list[int]:
    page_order = {page: set() for page in update}
    for x, y in rules:
        if x in page_order and y in page_order:
            page_order[y].add(x)

    # print(page_order)
    sorted_pages = sorted(update, key=lambda page: len(page_order[page]))
    # print(sorted_pages)
    return sorted_pages


def find_middle_pages_sum_2(reader: FileInputReader, word="XMAS") -> int:
    print(f"Reading file {reader.file_path}:")
    entire_content = reader.get_entire_content()
    rules, updates = parse_input(entire_content)

    incorrectly_ordered_updates = [update for update in updates if not is_update_correct(rules, update)]
    reordered_updates = [reorder_update(rules, update) for update in incorrectly_ordered_updates]
    middle_values = [update[len(update) // 2] for update in reordered_updates]
    total_middle_sum = sum(middle_values)

    print(f"Total middle sum {total_middle_sum}")
    return total_middle_sum


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert find_middle_pages_sum(reader_test) == 143
    assert find_middle_pages_sum(reader) == 5087


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert find_middle_pages_sum_2(reader_test) == 123
    assert find_middle_pages_sum_2(reader) == 4971


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
