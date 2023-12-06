# Error handling
# Author: Norbert Antal

import sys

filename = sys.argv[1]

try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)#(f"file {filename} does not exist")

