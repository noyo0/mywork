# myfunctions.py
# module of useful functions
# Author: Norbert Antal
'''Functrion returns the factorial number of an int 
ie. 7! = 7x6x5x4x3x2x1 = 5040'''

def factorial(num):
    if num == 1:
        return(1)
    factorial = 1
    for i in range(1,num+1):
        #print("before", factorial, "by", i)
        factorial *= i
        #print("after", factorial)
    return(factorial)

'''if __name__ == "__main__":
    print ("in MyFunctions", __name__)'''