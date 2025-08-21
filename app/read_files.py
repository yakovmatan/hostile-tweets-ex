import os


class ReadFile:

    def __init__(self, path):
        self.path = path


    def read_file(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"file not found: {self.path}")

        with open(self.path, "r") as file:
            return file.read()
