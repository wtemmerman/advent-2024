import os
import sys

import requests

from utils.get_cookie import get_aoc_session_cookie


def fetch_puzzle_input(day: int, session_cookie: str):
    """
    Fetch the puzzle input from Advent of Code and save it into the `inputs` directory.

    Args:
        day (int): The day of the puzzle (1-25).
        session_cookie (str): Your session cookie for Advent of Code authentication.

    Raises:
        ValueError: If the day is not between 1 and 25.
        Exception: If there's an issue fetching the input.
    """
    if day < 1 or day > 25:
        raise ValueError("Day must be between 1 and 25.")

    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}

    # Ensure the `inputs` directory exists
    os.makedirs("inputs", exist_ok=True)

    try:
        print(f"Fetching input for Day {day}...")
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            filename = os.path.join("inputs", f"day_{day}_input.txt")
            filename_test = os.path.join("inputs", f"day_{day}_input_test.txt")

            with open(filename, "w") as file:
                file.write(response.text.strip())
            print(f"Input saved to {filename}")

            with open(filename_test, "w") as file:
                file.write(response.text.strip())
            print(f"Test input saved to {filename_test}")
        else:
            raise Exception(
                f"Failed to fetch input: HTTP {response.status_code}. "
                "Ensure your session cookie is valid and you have unlocked this day's puzzle."
            )
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Replace this with your session cookie
    session_cookie = get_aoc_session_cookie()
    print(f"Fetched session cookie: {session_cookie}")

    if len(sys.argv) != 2:
        print("Usage: python script.py <day>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        fetch_puzzle_input(day, session_cookie)
    except ValueError:
        print("Please provide a valid day as a number between 1 and 25.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
