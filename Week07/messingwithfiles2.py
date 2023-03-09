import os

FILENAME ="messwithFiles.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line.strip())
else:
    print(FILENAME, "does not exists")

os.remove("data2.txt")
