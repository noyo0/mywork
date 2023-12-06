# how to raise and exception
# Author: Norbert Antal

try:
    input = input("enter number:  ")
    number=int(input)
    if (number < 0):
        raise ValueError("Negative value is entered")
    print(f"{number} multiplied by 2 is:", number * 2)
except ValueError as e:
    print(e)
    print("Please be positive")