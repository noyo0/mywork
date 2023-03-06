## ATU-Galway - Programming and Scripting
### Author: Norbert Antal
#### **pands-problem-sheet**
###### This "pands-problem-sheet" folder contains solutions for the weekly tasks.

---

- #### Week01
> w01_helloworld.py  
>> Program displays "Hello World!"

- #### Week02
> w02_bank.py
>> Program prompts the user and read in two money amounts in cents, adds the two amounts together and outputs the answer with a euro sign and decimal point between the euro and cent of the amount.
- #### Week03
> w03_waccounts.py
>> Program promts user for a 10 digit account number, reads in the account number and outputs 6 "X" letters and the last 4 digit of the account number give by the user. 

> w03_accounts2lenght.py
>> Similar to above but works with any lenght of account identification including numbers and letters, covers the first characters of any number with an "X" and displays the last 4 characters.
>>    ###### * References: 
>>###### 1. len function (https://www.geeksforgeeks.org/python-string-length-len/)  
>>###### 2. find certain section of a string (https://www.interviewqs.com/ddi-code-snippets/substring-python)

- #### Week04
> w04_collatz.py
>> Program asks user to input any positive integer and outputs the successive values of the following calculation; At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Program ends if the current value is one.
>>    ###### * References: 
>>###### 1. list item data types - ref: (https://www.w3schools.com/python/python_lists.asp)  
>>###### 2. print with custom dividers - ref: https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row

- #### Week05
> w05_weekday.py
>> Program checks if current date falls on a weekday or not, using the imported -datetime- module's date.weekday() function that returns the day of the week as an integer, where Monday is 0 and Sunday is 6. 
An if statement determines wether the current day represented as integer is a weekend day (larger than 4) otherwise it must be a weekday. Based on the if statement the appropriate message is printed.
There is no user interaction in this program.
>>    ###### * References: 
>>###### 1. datetime module - https://docs.python.org/3/library/datetime.html

- #### Week06
> w06_squareroot.py
>> Program finds approximate square root of a given number with Newton-Raphson Method
Created function "fn_newton" with two arguments; number, display. 
 "number" argument sets the number to calculate with, 
 "display" argument determines if the result is displayed as floating point number (default:0) or an integer (1)
Using the formula from reference below the program loops until maximum accuracy is reached;
    I noticed that while allowing infinite iterations of the square root calculation, Python limits the number of digits at 17 so the results are repeating once 17-digit accuracy is achieved.
    Exploiting this "feature" the program can store results in a container and check current result against previous iteration. 
    If the two are the same, the result must be the most accurate within this 17-digit restriction and the program can break out of the loop as there is no need to iterate any more.
As a failsafe in case for extreme large numbers a variable for maximum number of iterations is also established, with value set to 100.
User interaction provides the starting number where the Program insists on a positive number if negative is given, user also choses if the result is printed as integer or floating point number
>>    ###### * References: 
>>###### 1. Newton-Raphson Method: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/