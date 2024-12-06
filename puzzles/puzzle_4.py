import os

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)

DIRECTIONS = [
    (0, 1),  # Horizontal right
    (0, -1),  # Horizontal left
    (1, 0),  # Vertical down
    (-1, 0),  # Vertical up
    (1, 1),  # Diagonal down-right
    (1, -1),  # Diagonal down-left
    (-1, 1),  # Diagonal up-right
    (-1, -1),  # Diagonal up-left
]


def count_word_occurrences(reader: FileInputReader, word="XMAS") -> int:
    print(f"Reading file {reader.file_path}:")
    grid = reader.read_all_lines()
    # print(grid)

    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    total_count = 0

    # Helper to check if the word exists in a specific direction
    def search_direction(start_row, start_col, row_delta, col_delta):
        for i in range(word_len):
            r, c = start_row + i * row_delta, start_col + i * col_delta
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
                return 0
        return 1

    for row in range(rows):
        for col in range(cols):
            for row_delta, col_delta in DIRECTIONS:
                total_count += search_direction(row, col, row_delta, col_delta)

    print(f"Total count {total_count}")
    return total_count


def count_X_mas_occurrences(reader: FileInputReader) -> int:
    print(f"Reading file {reader.file_path}:")
    grid = reader.read_all_lines()
    # print(grid)

    rows, cols = len(grid), len(grid[0])
    total_count = 0

    def is_valid_mas(diagonal):
        """
        Check if the given diagonal is a valid MAS or SAM pattern.
        """
        return diagonal in [["M", "A", "S"], ["S", "A", "M"]]

    # Iterate over every possible center `A` in the grid
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == "A":  # Potential center of an X-MAS
                # Extract diagonals
                top_left_to_bottom_right = [
                    grid[row - 1][col - 1],
                    grid[row][col],
                    grid[row + 1][col + 1],
                ]
                top_right_to_bottom_left = [
                    grid[row - 1][col + 1],
                    grid[row][col],
                    grid[row + 1][col - 1],
                ]

                # Count valid diagonals
                if is_valid_mas(top_left_to_bottom_right) and is_valid_mas(top_right_to_bottom_left):
                    total_count += 1

    print(f"Total count {total_count}")
    return total_count


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert count_word_occurrences(reader_test) == 18
    assert count_word_occurrences(reader) == 2567


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert count_X_mas_occurrences(reader_test) == 9
    count_X_mas_occurrences(reader)


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
