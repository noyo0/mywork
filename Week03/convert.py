# convert.py
# Author: Norbert Antal
# Program takes in a float amount of dollars and returns that absolute amount in cent.

dollr = float(input("enter amount in $: "))
disp = int(abs(dollr)*100)
print(f"amoint in ¢:\t {disp}")