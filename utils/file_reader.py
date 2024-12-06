import os


class FileInputReader:
    def __init__(self, file_name: str):
        """
        Initialize the FileInputReader with the file name. Automatically appends
        the 'inputs/' directory to the file path.

        Args:
            file_name (str): Name of the input file (e.g., 'day_1_input.txt').
        """
        self.file_path = os.path.join("inputs", file_name)

    def read_line_by_line(self):
        """
        Read the file line by line and yield each line.

        Yields:
            str: A single line from the file.
        """
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
        except Exception as e:
            print(f"Error while reading the file: {e}")

    def read_all_lines(self):
        """
        Read all lines from the file into a list.

        Returns:
            list[str]: A list of all lines in the file.
        """
        try:
            with open(self.file_path, "r") as file:
                return [line.strip() for line in file]
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
        except Exception as e:
            print(f"Error while reading the file: {e}")
            return []

    def get_one_line(self):
        """
        Return all lines as a one line

        Returns:
            str: A string as one line
        """
        return "".join(self.read_all_lines())

    def process_lines(self, func):
        """
        Apply a function to each line in the file.

        Args:
            func (Callable[[str], Any]): A function to process each line.

        Returns:
            list[Any]: A list of results after applying the function to each line.
        """
        try:
            with open(self.file_path, "r") as file:
                return [func(line.strip()) for line in file]
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
        except Exception as e:
            print(f"Error while processing the file: {e}")
            return []
