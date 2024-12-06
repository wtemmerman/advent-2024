import sys
from puzzles import puzzle_1, puzzle_2, puzzle_3


def run_puzzle(day: int):
    puzzle_mapping = {
        1: puzzle_1.run,
        2: puzzle_2.run,
        3: puzzle_3.run,
    }
    if day in puzzle_mapping:
        print(f"Running Puzzle {day}...")
        puzzle_mapping[day]()
    else:
        print(f"Puzzle for Day {day} is not implemented yet.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <day>")
        sys.exit(1)
    day = int(sys.argv[1])
    run_puzzle(day)