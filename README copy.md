## ATU-Galway - Programming and Scripting
### Author: Norbert Antal
#### **pands-problem-sheet**
###### This "pands-problem-sheet" folder contains solutions and documentation for the weekly tasks.

---

### Contents
- Week01: Hello World
- Week02: Bank
- Week03: Accounts
- Week04: Collatz
- Week05: Weekday
- Week06: Square root

---

#### Week01: Hello World
> w01_helloworld.py  

    Task:
    "Commit and push a file to the problem sheet called helloworld.py"

> ##### Program displays "Hello World!"

#### Week02: Bank
> w02_bank.py
 
    Task:
    "Write a program called bank.py 
    The program should: 
    - Prompt the user and read in two money amounts (in cent)
    - Add the two amounts
    - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount"

> Program prompts the user to type in two money amounts in cents and stores them in 2 variables "amount1" and "amount2". The program adds the two values together and divides the sum by 100 thus converting the cent values to euro and outputs the answer with a euro sign and decimal point between the euro and cent of the amount.

#### Week03: Accounts
> w03_waccounts.py

    Task:
    "Write a python program called accounts.py that reads in
    a 10 character account number and outputs the account number
    with only the last 4 digits showing 
    (and the first 6 digits replaced with Xs)."

> Program promts user for a 10 digit account number, then devides the number by 10,000 to get the last 4 digits with a modulo operator and stores the value in a variable. Program than prints out 6 "X"characrters followed by the 4 digits stored in the variable.
> #### Week03: Extra
> w03_accounts2lenght.py
 
    Extra: 
    "Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)"

> The modified program promts user for a 10 digit account number, then check lenght of the given number using the len function and deducts 4 to establish how many characters of the accoun t number must be replaced with "X". The result is then stored in variable "coverlenght". The program then converts the original number to string and stores it in variable "accstr" so it can be concatenated and its individual characters can be called between a range. Finally the program concatenates as many "X" caracters as the value stored in coverlenght and calls the last 4 digits from "accstr" by referring to the range from position that equals coverlenght to position that equals coverlenght + 4.
Since the user entry is stored and manipulated as string, there is no limitations to numbers only, the program can deal with any character.
>>    ###### * References: 
>>###### 1. len function (https://www.geeksforgeeks.org/python-string-length-len/)  
>>###### 2. find certain section of a string (https://www.interviewqs.com/ddi-code-snippets/substring-python)

#### Week04: Collatz
> w04_collatz.py

    Task:
    "Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
    At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
    Have the program end if the current value is one."

>> Program asks user to input any positive integer which is stored as integer in variable "number". A list "numbers" is created where each result of the calculation will be stored. The calculation is a formula to calculate each member of a Collatz sequence. The program assumes the endpoint of a Collatz seqence is always 1 (until proven otherwise) so a while loop is initiated which breaks when the result of the calculation reaches 1. Whithin the while loop 
>> 
>> and outputs the successive values of the following calculation; At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Program ends if the current value is one.
>>    ###### * References: 
>>###### 1. list item data types - ref: (https://www.w3schools.com/python/python_lists.asp)  
>>###### 2. print with custom dividers - ref: (https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row)
>>###### 3. Collatz conjencture - ref: (https://en.wikipedia.org/wiki/Collatz_conjecture)

#### Week05: Weekday
> w05_weekday.py
>> Program checks if current date falls on a weekday or not, using the imported -datetime- module's date.weekday() function that returns the day of the week as an integer, where Monday is 0 and Sunday is 6. 
An if statement determines wether the current day represented as integer is a weekend day (larger than 4) otherwise it must be a weekday. Based on the if statement the appropriate message is printed.
There is no user interaction in this program.
>>    ###### * References: 
>>###### 1. datetime module - (https://docs.python.org/3/library/datetime.html)

#### Week06: Square root
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
>>###### 1. Newton-Raphson Method: (https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)
