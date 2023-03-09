# messing with files
#author: Norbert Antal
FILENAME = "2BR02B_K.Vonnegut.txt"

with open(FILENAME,"r") as f:
    for data in f:
        print(data.strip())
