import sys


class ChangeOutput:
    def __init__(self):
        self.old_stdout = sys.stdout
        self.output_file = open("./stdout.txt", "w")

    def __enter__(self):
        sys.stdout = self.output_file

    def __exit__(self, *args):
        self.output_file.close()
        sys.stdout = self.old_stdout


class ChangePrint:
    def __init__(self):
        self.old_print = print
        self.output_file = open("./stdout.txt", "w")

    def __enter__(self):
        def my_print(*args, **kwargs):
            kwargs["file"] = self.output_file
            self.old_print(*args, **kwargs)

        return my_print

    def __exit__(self, *args):
        global print
        print = self.old_print


print("tata")
with ChangePrint() as print:
    print("a l'intérieur")
print("à l'extérieur")

import contextlib

contextlib.contextmanager
