import sys

old_stdout = sys.stdout
sys.stdout = open("./stdout.txt", "w")
print("tata\n")
