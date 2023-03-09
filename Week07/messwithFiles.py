# messing with files
#author: Norbert Antal
FILENAME = "data.txt"
"""
with open(FILENAME,"r") as f:
    for data in f:
        print(data.strip())
"""
with open("data2.txt", "w+") as f:
    f.write("data2 text\n")
    f.write("\ndata2 line 2\n")
    f.seek(0)

    data = f.read()
    print(data)

print("done")
