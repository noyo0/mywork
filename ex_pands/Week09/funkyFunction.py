# this is the Fibonacci function 
#Author: Norbert Antal

import logging
logging.basicConfig(level=logging.DEBUG)

# -------- Fibonacci function ------------
def Fibonacci(num):
    if num == 0:
        return []
    if num == 1:
        return [0]
    if num < 0:
        raise ValueError('number must be a positive number')
    Fibonacci=[0,1]
    calc=0
    for f in range(0,num-2):
        calc=Fibonacci[-1]+Fibonacci[-2]
        Fibonacci.append(calc)
        #print(calc)
    return(Fibonacci)

# ---- smooth running tester -------
if __name__ == '__main__':
# tests will go here
    print("all good")

#------ test with assertion --------
return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert Fibonacci(7) == return7, 'incorrect return for 7'
assert Fibonacci(11) == return11, 'incorrect return for 11'
assert Fibonacci(0) == [], 'incorrect return value for 0'
assert Fibonacci(1) == [0], 'incorrect return value for 1'

'''try:
    Fibonacci(-1)
except ValueError:
    pass
else:
    assert False, "Fibonacci missing valueError"'''







