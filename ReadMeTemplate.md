# Problems 2020


This repository is used for the problem sets given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.\
Here I will explain how I came to the solution of given tasks, reference the sources I researched for solving the problems and list the technologies I used for creating and testing the code.\
I have previous knowledge and understanding of basics of coding in python so for some tasks I didn't require extensive research.


## Table of contents
* [Weekly tasks](#weekly-tasks)
    * [BMI](#bmi)
    * [Second string](#second-string)
    * [Collatz](#collatz)
    * [Weekday](#weekday)
    * [Square root](#square-root)
    * [Es](#es)
    * [Plotting](#plotting)
* [Technologies](#technologies)


Weekly tasks
======
### ***BMI***

    Write a program that calculates somebody's Body Mass Index (BMI). 
    The inputs are the person's height in centimetres and weight in kilograms. 
    The output is their weight divided by their height in metres squared. 

This program is a basic calculation of a given formula based on the users input.

User inputs the height in centimeters and weight in kilograms. The challenge here is not to forget to convert height from centimeters to meters in order to get the correct answer.

Even though the formula could be done in one line, this way is chosen to simplify the calculation by adding a new variable *hm*. This variable is used for converting height from centimeter to meters.

The [rounding](https://www.geeksforgeeks.org/round-function-python) of the result to 2 points was added for a nicer touch. The idea goes to another student.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 2-bmi.py
```
User input :
```
Enter your weight in kg: 80
Enter your height in cm: 180
```
and the output is :

```
Your BMI is 24.69
```
</p>
</details>

- - - -

  ### ***Second string***

    Write a program that takes asks a user to input a string and outputs every second letter in reverse order. 

There are couple of ways to solve this problem, but the method of slicing is chosen because it's simple and only one line of code. The idea was found on [Geeksforgeeks.org](https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/).

The syntax of slicing is:
``` 
[start:stop:step]
```
*Start* and *stop* are default values as we need the whole sentence. *Step* is negative because we need the string in the reverse order. The value is 2 because we need every second letter from the reversed order.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 3-secondstring.py
```
User input :
```
Enter a sentence: A large fawn jumped quickly over white zinc boxes.
```
and the output is :

```
.eo nzeiwrv lcu emjna ga
```
</p>
</details>

----

  ### ***Collatz***
    
    Write a program that asks the user to input any positive integer and outputs the successive 
    values of the following calculation. At each step calculate the next value by taking the 
    current value and, if it is even, divide it by two, but if it is odd, multiply it by three 
    and add one. Have the program end if the current value is one.

Even though the task didn't require to have a fix for wrongly inputed negative number, it's added to avoid errors. This is done with *while* loop.

In second *while* loop we are cheching whether a number is odd or even, with the help of conditional statements *if* and *else* and it's doing so until the current value is one.\
The statement *if* checks if the number is even using modulus operation. If the remainder of the operation is zero, the number is even and the program divides the number by 2 and prints it out.\
If the remainder is not zero, program performs operations from statement *else* - multiplying the number by three and adding one, and prints out the result.

The output of the program looks neater if it's written in one line. That is done with the help of *end = " "* parameter, and the reference goes to [Geeksforgeeks.org](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/).

<details>
           <summary>User point of view</summary>
           <p>
         
User call of the program is :

```
λ python 4-collatz.py
```
User input :
```
Add any positive integer: -20
```
In case of putting in a negative integer the program will respond with a message that a number is negative and ask to input a positive integer until the input is correct:
```
Add any positive integer: -10
-10 isn't a positive integer.
Add any positive integer: -20
-20 isn't a positive integer.
Add any positive integer: 20
```

When user inputs the positive integer the output is :

```
20 10 5 16 8 4 2 1
```
</p>
</details>

----

  ### ***Weekday***

    Write a program that outputs whether or not today is a weekday.

For this program it is neccessary to import *datetime* module so we can manipulete date and time.

Even though the Programming and scripting [video](https://web.microsoftstream.com/video/77f26693-82ed-4006-8c22-c61d37e2f77f) gave the initial idea, a little bit of research on [Python documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.now) helped to crack the code.\
There it was found that by implementing *date.weekday()*, where Monday is 0 and Sunday is 6, it can easily be checked, with the help of *if* statement, whether today is weekday or weekend.

It's important to run the program on both the weekday and weekend to get a correct result.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 5-weekday.py
```
This program does not requre any user input, it just outputs the result.
On the weekday result is:
```
Yes, unfortunately today is a weekday.
```
On the weekend result is:
```
It is the weekend, yay!
```
</p>
</details>

----

  ### ***Square root***

    Write a program that takes a positive floating-point number as input and outputs an 
    approximation of its square root.
    You should create a function called sqrt that does this.

Addition to the task: 
    
    The weekly task is trickier than the previous ones but I really suggest you try to crack it.
    You'll find a simple algorithm for the problem if you Google "Newton's method for square roots".
    I really recommend trying to code it up yourself rather than looking at others' implementations.

This program required hours of research. Websites used for research and understandig are [Geeksforgeeks.org](https://www.geeksforgeeks.org/program-for-newton-raphson-method/), [StackOverflow](https://stackoverflow.com/questions/12850100/finding-the-square-root-using-newtons-method-errors), [Hackernoon](https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo), [Math.ubc.ca](https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/), but the most helpfull one was a Youtube video by [Mechtutor com](https://www.youtube.com/watch?v=szQUIRPrAgQ). 

The most challenging part was the understanding how the method works, and the coding after that was just implementing mathematical formulas.

Like in the Collatz task, here I also implemented checking if the user input indeed is the positive floating-point number. This was done with an *if* statement checking if the number was smaller than zero. If it is, number was changed into a postive one using absolute value with the help of *abs()* function.

Function was created with a keyword *def sqrt()*, and later called with the keywords *sqrt(x)*. In the function variable *n* is defined as an initial guess that first iteration equals to the number we want to root (variable *x* that was the user input). Next, *while* loop is checking 2 conditions of convergence. When conditions are no longer true, function returns the value of variable *x*. Function is called when the result is outputed.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 6-squareroot.py
```
User input :
```
Input positive floating-point number: -20.5
```
In case of putting in a negative integer the program will respond with a message that a number is negative and fix it for the user, giving the output straight away as well:
```
Oops, your input is a negative number. I'm sure it's a mistake.
I'll fix it for you: 20.5
The square root of  20.5 is approx.   4.528
```
</p>
</details>

- - - -

  ### ***Es***

    Write a program that reads in a text file and outputs the number of e's it contains.
    The program should take the filename from an argument on the command line. 

This program reads a text file called by user as an argument in the command line. The requirement is that a requested file is in the same directory (folder) as is this program.

To make that possible *sys* method was imported. Using the *sys.argv[1]* variable, it is defined that the filename is second argument when calling a program ( *sys.argv[0]* is the program we are trying to start ).\
References for this part of program go to [Python documentation](https://docs.python.org/3.8/library/sys.html) and [Geeksforgeeks.org](https://www.geeksforgeeks.org/command-line-arguments-in-python/#sys).

With the *open( filename,'r' )* function we are opening a file that we called in the command line argument, and making it available just for reading.
For counting the lower case letter 'e' the method *count()* was used, and the argument is a string *"e"*. Reference for the *count()* method is [Programiz](https://www.programiz.com/python-programming/methods/string/count).

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 7-es.py moby-dick.txt
```

Output is simply the number of letter "e" in the called file :

```
116960
```
</p>
</details>

- - - -

  ### ***Plotting***
    
    Write a program that displays a plot of the functions f(x)=x, g(x)=x2
    and h(x)=x3 in the range [0, 4] on the one set of axes. 

This task was very interesting to do.\
For creating this program ipython was used to find the best solution. The best results were chosen with the help of ipython log created by the argument *%logstart* in ipython.\
The reference for this program was [video](https://web.microsoftstream.com/video/41d1fabf-4b40-416d-babf-ee949521d3b9?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D1598) from the module page on Learnonline.

To do the plot libraries *numpy* and *matplotlib.pyplot* had to be imported.\
Variables *f*, *g* and *h* in the program define mathematical functions f(x), g(x) and h(x) from the task respectively.\
Range was defined with the help of *arange()* function from *numpy* library. Since the range set in the task is [0.4], the step chosen for creating a nice looking plot is 0.1.
The title, and both the x and y axis were labeled using the functions *title()*, *xlabel()* and *ylabel()* respectively from the *matplotlib.pyplot* library.\
The plot is done with the help of dots - green for f(x), blue for g(x) and red for h(x). Tho help the user know which function is shown with which color, legend was created.

The output of this task for the user is a saved image of the plot in the same directory (folder) as the program creating the plot.
<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 8-plotting.py
```

Output is the picture which should look like this:

![alt text](https://raw.githubusercontent.com/sandraelekes/GMIT-ps/master/8-plotting.png "Result of plotting")

</p>
</details>

- - - -

Technologies
====

  * Visual Studio Code - version 1.43.2
  * Cmder - version 1.3.14.982


