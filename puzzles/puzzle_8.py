import os
from math import gcd

from utils.file_reader import FileInputReader
from utils.helper import get_puzzle_number

# Get the current filename
filename = os.path.basename(__file__)
number = get_puzzle_number(filename)


def parse_map(grid):
    """Parse the grid to find antennas and their positions."""
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():  # Only consider antennas with valid frequencies
                antennas.setdefault(char, []).append((x, y))
    return antennas


def find_unique_antinodes(reader: FileInputReader) -> int:
    grid = reader.read_all_lines()
    antennas = parse_map(grid)
    antinodes = set()
    max_x, max_y = len(grid[0]), len(grid)

    # print(antennas)
    for _, positions in antennas.items():
        # Iterate through all unique pairs of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1, p2 = positions[i], positions[j]
                # Calculate the two antinodes
                q1 = (2 * p2[0] - p1[0], 2 * p2[1] - p1[1])
                q2 = (2 * p1[0] - p2[0], 2 * p1[1] - p2[1])
                # Check if they are within grid bounds
                if 0 <= q1[0] < max_x and 0 <= q1[1] < max_y:
                    antinodes.add(q1)
                if 0 <= q2[0] < max_x and 0 <= q2[1] < max_y:
                    antinodes.add(q2)

    print(f"Total valid antinodes: {len(antinodes)}")
    return len(antinodes)


def get_standard_line(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int, int]:
    x1, y1 = p1
    x2, y2 = p2

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    # Normalize coefficients
    g = gcd(gcd(abs(A), abs(B)), abs(C))
    if g != 0:
        A //= g
        B //= g
        C //= g

    # Ensure A is non-negative
    if A < 0 or (A == 0 and B < 0):
        A = -A
        B = -B
        C = -C

    return (A, B, C)


def find_unique_antinodes_v2(reader: FileInputReader) -> int:
    grid = reader.read_all_lines()
    antennas = parse_map(grid)
    antinodes = set()
    max_x, max_y = len(grid[0]), len(grid)

    for _, positions in antennas.items():
        if len(positions) < 2:
            continue  # Need at least two antennas to form a line

        # Find all unique lines that contain at least two antennas
        lines: set[tuple[int, int, int]] = set()
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                p1, p2 = positions[i], positions[j]
                line = get_standard_line(p1, p2)
                lines.add(line)

        # For each line, iterate through grid points and add those that lie on the line
        for line in lines:
            A, B, C = line
            if A == 0 and B == 0:
                continue  # Invalid line
            if B == 0:  # Vertical line
                x = -C // A if A != 0 else 0
                if A != 0 and -C % A == 0:
                    for y in range(max_y):
                        q = (x, y)
                        if 0 <= x < max_x:
                            antinodes.add(q)
            elif A == 0:  # Horizontal line
                y = -C // B if B != 0 else 0
                if B != 0 and -C % B == 0:
                    for x in range(max_x):
                        q = (x, y)
                        if 0 <= y < max_y:
                            antinodes.add(q)
            else:
                for x in range(max_x):
                    # Compute y using the line equation Ax + By + C = 0 => y = (-A*x - C)/B
                    numerator = -A * x - C
                    if numerator % B == 0:
                        y = numerator // B
                        if 0 <= y < max_y:
                            q = (x, y)
                            antinodes.add(q)

    print(f"Total valid antinodes: {len(antinodes)}")
    return len(antinodes)


def part1():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert find_unique_antinodes(reader_test) == 14
    assert find_unique_antinodes(reader) == 308


def part2():
    reader_test = FileInputReader(f"day_{number}_input_test.txt")
    reader = FileInputReader(f"day_{number}_input.txt")

    assert find_unique_antinodes_v2(reader_test) == 34
    assert find_unique_antinodes_v2(reader) == 1147


def run():
    print("Start part 1")
    part1()

    print("\nStart part 2")
    part2()
