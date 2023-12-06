# list.py
# Author: Norbert Antal
# messing with list
# https://docs.python.org/3/tutorial/datastructures.html


#x="StarDestroyer"
#boats = ["long", "short,",x,12,"gerappa",45]
#print(f"this is your list {boats}")

"""
x = 0
ages = [1,2,3,4,5,66]
for i in ages:
    x += i
print(x, "lenght",len(ages))
"""

teststring =[1,2,3,4,5,6,7,8,9,0]
print(*teststring[::-2])
teststring[1] = 900
print(*teststring)

