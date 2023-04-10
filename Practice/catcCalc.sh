#!/bin/bash

# catcCalc.sh
# A program to generate math table (range restricted to 1-15) for a hypothetical student

# Author: Norbert Antal

# Starting points of the solution
# 	simple calculator ref: https://www.geeksforgeeks.org/simple-calculator-bash/
# 	number table ref: https://www.geeksforgeeks.org/shell-script-to-print-table-of-a-given-number/
# 	working syntax for arithmetics ref: https://linuxconfig.org/bash-scripting-operators
# 	compare strings with if statement ref: https://linuxize.com/post/how-to-compare-strings-in-bash/

# Using shellscript functions for easy readibility and more practical user interaction mamagement
# 	shellscript functions ref: https://www.shellscript.sh/functions.html

# ---------- The main function of the program is the calculator. It is encapsulated within a function fncalculator() for easier read and edit.
fncalculator()
{
# ------------------------- fncalculator() workings---------------------

# Operation selected with a chain of if and elif functions checking for matching string value  from user imput stored in the 'operator' variable (see later)
# Once 'operator' equals the operator symbol in one of the if or elif  statements, the  program enters a while loop under the statement 
#	 that is True while the iterator variable 'i' is within the range of 1-15. 
#	Inside the while loop an echo command outputs the statement and result of the  mathematical operation corresponding to the if statement's string comparison 
# 	 the arithmetic operation is carried out using the value of 'operand' thaken from user entry (see later) as first operand
#	 and the value of the iterator variable 'i' as the second operand for each iternation.
#	In the next line the iterator is increased by 1.
#	The echo command with the calculation within the while loop repeated with each new iteration of 'i' value 
#	 until the while statement is False or until value of 'i' reaches 15 that is


    i=1 #initialising loop with starting value = 1
    
    clear #clear screen before result output for aesthatic reasons

    echo "Math table of $operand $operator range of 1-15" # user interaction - output label
    
    #Addition
    if [[ "$operator" == "+" ]] #compare strings stored in "operator" (from user entry) 	
    then # if match, jump to the while loop below
	while (( $i <= 15 )) # loop while until value of 'i' 15        
        do #if while is True carry out commands below
            echo "$operand + $i = $(($operand + $i))" # output command with arithmetic statement and result. See output structure detailed below:
	    #first operand(from user input stored as 'operand'),operator symbol, second operand (current iteration stored in 'i') 
	    # an equal symbol and the result of the calculation with the two varaibles
            ((++i)) # increase value of i by 1 
    done # end of if statement
    
    #Substraction
    elif [[ "$operator" == "-" ]] #program runs this or subsequent elif statement similar in structure (with differnt arithemtics) until value of 'operator' equals to the string in the conditional statement
    then
	while  (($i <= 15 ))
        do
            echo "$operand - $i = $(($operand - $i))"
            ((++i))
        done
    
    #Multiplication
    elif [[ "$operator" == "*" ]] # 
    then
	while (($i <= 15 ))
        do
            echo "$operand * $i = $(($operand * $i))" 
            ((++i))
        done
    
    #Division    
    elif [[ "$operator" == "/" ]]
    then
	    while (( $i <= 15))
        do
            #Shell Script does not provide native  support for floating point arithmetic ref: https://linuxhint.com
	    # However, BC (Basic Calculator) if installed, can provide this function. --> ref: stackowerflow.com
	    # As BC  is installed on this server (checked with "type bc" command) so floating point output is possible, therefore this Division operation will output floating point results.
	    echo "$operand / $i = $(echo "scale=4; $operand / $i" | bc | sed 's/^\./0./' )" #format to output result in floating point (4 digit accuracy) --> ref: stackoverflow.com
	    ((++i))
        done
    
    #Exponentiation    
    elif [[ "$operator" == "^" ]]
    then
	    while(( $i <= 15))
        do
            echo $operand ^ $i = $[ $operand ** $i ] 
	    ((++i))
        done
    else
	#userinteraction if user enters a string into 'operator' that is not one of the available operators    
        clear # clear screen for aesthetics 
        echo "Invalid operator entered. Program terminated - try running the program again..."
	echo "Accepted operators are: + - * / ^ "
	echo "..."
    fi #end of if statement
} # edn of fncalculator() function

# For easy reuseability purposes user entry validation is encapsulated into a function: fnantryvalid()

# ------------------------ fnentryvalid() function workings -------------------

# operand entry  user interaction and value  validation
fnentryvalid()
{
# User interaction - ask for value for 'operand' variable
echo "Please enter operand within 1-15"
    read operand # store value in 'operand' variable for later use in fncalculator function

    if (($operand >= 1 && $operand <= 15)); then #if entry is valie (within the range of 1-15) call the calculator function
        fncalculator
    else
        echo "Invalid input, number must be in range (1-15)."
        fnentryvalid # using shellscript function to be able to reuse validation without the program exiting
fi #end of if statement
} # end of fnentryvalid() function

# ------------------------ PROGRAM STARTS -------------------------------------

# User interacrtion -  list out all available options and indicate acceptable entries
echo "Enter the symbol for the mathematical operation you want to perform:"
echo "Addition (+)"
echo "Subtraction (-)"
echo "Multiplication (*)"
echo "Division (/)"
echo "Exponent (^)"
read operator # store user entry for later use in fncalculator function

#User interaction - ask user for an operand and indicate acceptable range
echo "Please enter operand within 1-15"
read operand #store entry in variable 'operand' for later use in fncalculator function
# check valid entry -->> ref: stackoverflow.com
if (($operand >= 1 && $operand <= 15)); then #check if user entered number between range 1-15
    clear #clear the terminal
  fncalculator #use function so script easier to read
else
#User interaction -  error message and remind user what the acceptabnle range is
  echo "Invalid input, number must be in range (1-15)." #if entry invalid, restart function by calling itself
  fnentryvalid
fi


# Thiswasalotofsweatswearsandtears

