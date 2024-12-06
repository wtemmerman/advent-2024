# Advent 2024

Just some code to enjoy the Advent 2024: https://adventofcode.com/2024/

### To get input of puzzle:
> python utils/get_puzzle.py 1

This will create a `.txt` file in the inputs folder. Also, a test input is created in addition of the main puzzle input, for test purpose.

### To run a solution
> python main.py 1

You need to update the mapping in `main.py` and have a `puzzle_X.py` (X as the day parameter) present in `puzzles` folder

### Issue with session cookie
If you have problem with `get_aoc_session_cookie` just replace, in `get_puzzle.py` line 56:
> session_cookie = get_aoc_session_cookie()
 
with 
 
> session_cookie = "YOUR_SESSION_STRING"