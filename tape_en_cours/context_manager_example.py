import sys


class ChangeOutput:
    def __init__(self):
        self.old_stdout = sys.stdout
        self.output_file = open("./stdout.txt", "w")

    def __enter__():
        sys.stdout = self.output_file

    def __exit__(self, *args):
        self.output_file.close()
        sys.stdout = self.old_stdout


print("tata")
with ChangeOutput():
    print("a l'intérieur")
print("à l'extérieur")
