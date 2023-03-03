# squareroot.py
# Author: Norbert Antal
# Program finds square root of a givennumber with Newton-Raphson Method
# Created function "fn_newton" with three arguments; number, accuracy, display. 
# "number" argument sets the number to calculate with, 
# "accuracy" determines maximum number of digits (default:17), 
# "display" argument determines if the result is displayed as floating point number (default:0) or an integer (1)
# Program runs until max accuracy is reached;
# I noticed that while infinite iterations, python limits the number of digits at 17 and after reaching max accuracy the results are repeating.
# Exploiting this "feature" the program can store results in a container and check current result against previous iteration. 
# If the two are the same, there is no need to iterate any more, the result is the most accurate and final.
# ref: Newton-Raphson Method: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# ------------------------------fn_newton-------start--------
def fn_newton(number,acc=17,disp=0):
    i=0
    itr=100 #maximum number of iterations to optimise resources with extreme large numbers
    x=number #starting number as per user input
    res=[] # result container to find the most accurate approximation
    while i<itr:
        x=round((x+number/x)/2,acc) # Calculating the Square Root of a Number using the Newton-Raphson Method, "acc" variable is limiting number of digits as per user's accuracy input
        i+=1
        if x not in res: # checks if result is repeating (after reaching max accuracy I found the results repeating and to be limited at 17 digits)
            res.append(x) # if not, adds stores it in the result container acc[]
        else:# if result is the same stored result from previous iteration, the current result is the most accurate, the program continues to the return function
            if disp==1: #check if user defined result display method (int or float)
                return(int(x)) # if user chose int, result returns as int
            else:
                return(x)  # if user chose float (or left the second argument blank), result returns as float
# -----------------------------fn_newton---------end-----------

print("""
Square root function "fn_newton()" takes 3 arguments "fn_newton(number, accuracy, display)"
    - number - is a positive floating point number to find the square root for
    - accuracy - sets the accuracy between 1-17 digits
    - display - determines if the result is displayed as an integer or a floating point number""")
n=float(input("Please enter a positive floating-point number: ")) # user prompted for a positive floating point number
while n<=0: # program will wex the user until positive number is given
    n=float(input("...but seriously, please enter a positive floating-point number: ")) 
acc=int(input("Default accuracy is 17 digits, do you want to increase? Enter a number between 10-17: "))
while acc not in range(10,18):
    acc=int(input("a number between 10-17 please: "))
f=str(input("Do you want the result as a floating point(Yes?): ")) # User prompted for display method
if f== "Y" or f=="y" or f=="yes" or f=="Yes": # Program allows for few variations of "yes" entries for Floating point display, everything else results in integer display
    f=0
else:
    f=1
p=fn_newton(n,acc,f) # setting variable p for printing the result
print(f"\n\nthe square root of {n} is approximately: {p}") #result is printed as per user interaction
