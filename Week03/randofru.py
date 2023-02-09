import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print(f"A Random Fruit:{fruit}")