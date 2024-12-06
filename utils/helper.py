import re


def get_puzzle_number(filename: str) -> int:
    # Extract the number using a regular expression
    match = re.search(r"\d+", filename)

    if match:
        number = int(match.group())  # Convert the extracted number to an integer
        return number
    else:
        print("No number found in the filename.")
