import copy
import os
from collections import defaultdict

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)


def parse_map(grid: list[str]) -> tuple[tuple[int, int], str]:
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in "^>v<":
                return (r, c), cell
    raise ValueError("Guard not found on the map")


def simulate_guard(grid, start_pos, direction):
    rows, cols = len(grid), len(grid[0])
    visit_count = defaultdict(int)  # Tracks how many times each position is visited
    directions = {
        "^": (-1, 0),  # up
        ">": (0, 1),  # right
        "v": (1, 0),  # down
        "<": (0, -1),  # left
    }
    turn_right = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }

    r, c = start_pos
    visit_count[(r, c)] += 1

    while True:
        dr, dc = directions[direction]
        next_r, next_c = r + dr, c + dc

        # Check if the guard is out of bounds
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        # Check if there is an obstacle
        if grid[next_r][next_c] == "#":
            direction = turn_right[direction]  # Turn right
        else:
            # Move forward
            r, c = next_r, next_c
            visit_count[(r, c)] += 1

    return len(visit_count)


def simulate_guard_loop(grid, start_pos, direction, new_obstruction=None):
    rows, cols = len(grid), len(grid[0])
    directions = {
        "^": (-1, 0),  # up
        ">": (0, 1),  # right
        "v": (1, 0),  # down
        "<": (0, -1),  # left
    }
    turn_right = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }

    # Add the new obstruction to the grid if specified
    if new_obstruction:
        r_obs, c_obs = new_obstruction
        if grid[r_obs][c_obs] == "#":
            return False  # Already an obstacle, no loop
        grid[r_obs][c_obs] = "#"

    r, c = start_pos
    visited_states = set()
    current_state = (r, c, direction)
    visited_states.add(current_state)

    while True:
        dr, dc = directions[direction]
        next_r, next_c = r + dr, c + dc

        # Check if the guard is out of bounds
        if not (0 <= next_r < rows and 0 <= next_c < cols):
            break

        # Check if there is an obstacle
        if grid[next_r][next_c] == "#":
            direction = turn_right[direction]  # Turn right
        else:
            # Move forward
            r, c = next_r, next_c
            current_state = (r, c, direction)

            if current_state in visited_states:
                # Loop detected
                return True

            visited_states.add(current_state)

    return False


def count_guard_position(reader: FileInputReader) -> int:
    grid = reader.read_all_lines()
    # print(grid)
    start_pos, direction = parse_map(grid)
    total_guard_position = simulate_guard(grid, start_pos, direction)

    print(f"Total guard positon: {total_guard_position}")
    return total_guard_position


def count_position_to_block(reader: FileInputReader) -> int:
    grid = [list(line) for line in reader.read_line_by_line()]
    # print(grid)
    start_pos, direction = parse_map(grid)
    rows, cols = len(grid), len(grid[0])
    total_position_to_block = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) == start_pos or grid[r][c] != ".":
                continue  # Skip starting position and existing obstructions

            # Check if placing an obstruction here causes a loop
            grid_copy = copy.deepcopy(grid)
            causes_loop = simulate_guard_loop(grid_copy, start_pos, direction, new_obstruction=(r, c))
            if causes_loop:
                total_position_to_block += 1
                # print(f"Obstruction at ({r}, {c}) causes a loop.")

    print(f"Total position to block: {total_position_to_block}")
    return total_position_to_block


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert count_guard_position(reader_test) == 41
    assert count_guard_position(reader) == 4374


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert count_position_to_block(reader_test) == 6
    assert count_position_to_block(reader) == 1705


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
