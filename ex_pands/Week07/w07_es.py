# w07_es.py
# Author: Norbert Antal
# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line. 
# Strip ref: https://www.w3schools.com/python/ref_string_strip.asp#:~:text=The%20strip()%20method%20removes,default%20leading%20character%20to%20remove)
# count occurence ref: https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/
# Command line Arguments with sys module ref: https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv#:~:text=argv%3F-,sys


import sys # module to use Command line arguments

FILENAME = sys.argv[1] # passing second argument (first is always the filename in sys)
count = 0 #setting counter to 0
with open(FILENAME, "rt") as f: # reading in file with filename passed from command line argument as "f"
        for data in f: # reading each line in f and storing as "data"
            text = data.strip() #removing leading and trailing characters and storing stripped in "text"
            for t in text: # cycling through each character in text and storing as "t"
                if t == "e": # checking if current character in "t" is an e character
                    count += 1 #if yes, increase count by one
        print(count) #print accumulated value of "count"