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
        self.old_stdout = sys.stdout
        self.output_file = open("./stdout.txt", "w")

    def __enter__(self):
        sys.stdout = self.output_file

    def __exit__(self, *args):
        self.output_file.close()
        sys.stdout = self.old_stdout


print("tata")
try:
    with ChangeOutput() as print:
        print("a l'intérieur")
        1 / 0
except:
    pass
print("à l'extérieur")
