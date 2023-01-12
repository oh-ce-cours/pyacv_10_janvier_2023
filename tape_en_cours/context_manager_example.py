import sys

old_stdout = sys.stdout
sys.stdout = open("./stdout.txt", "w")
print("toto\n")
sys.stdout.flush()
sys.stdout.close()
