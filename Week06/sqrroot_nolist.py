# -------fn_newton------------------------start

def fn_newton(number,disp=0):
    i=0
    itr=100 #maximum number of iterations in case of extreme large numbers (probably overkill)
    x=number #starting number as per user input
    res=0 # result container to find the most accurate approximation
    while i<itr:
        x=0.5*(x+number/x) # Calculating the Square Root of a Number using the Newton-Raphson Method
        i+=1 # increase iteration counter by 1
        if x != res: # checks if results are repeating
            res = x # if not, stores result in the result container "res[]" and continues with the loop
        else:# if result equals stored result from previous iteration, the current result is the most accurate, the program continues to the return function
            if disp==1: #check if user defined result display method (int or float)
                return(int(x)) # if user chose int, result returns as int
            else:
                return(x)  # if user chose float (or left the second argument blank), result returns as float
            
# -------fn_newton------------------------end

# user interaction ---------
n=float(input("Please enter a positive floating-point number: ")) # user prompted for a positive floating point number
while n<=0: # program will wex the user until positive number is given
    n=float(input("...please enter a positive floating-point number: ")) 
f=str(input("Do you want the result as an integer (Yes?): ")) # User prompted for display method
if f== "Y" or f=="y" or f=="yes" or f=="Yes": # Program allows for few types of "yes" entries for Floating point display, everything else results in integer display
    f=1
else:
    f=0
p=fn_newton(n,f) # setting value for "p" by calling function fn_newton with arguments defined by user interaction
print(f"\n\n The square root of {n} is approximately: {p}") #starting number and approximate square root is printed as per user interaction
