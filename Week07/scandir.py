import os
dirlist=os.scandir('textfiles/')
for d in dirlist:
    print(d)