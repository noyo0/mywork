import random

randrange1 = int(input("let's generate a random number \nfrom: "))
randrange2 = int(input("to: "))
number = random.randint(randrange1,randrange2)
print ("Here is a random number within the range between {} and {}: \n{}". format(randrange1,randrange2,number))
