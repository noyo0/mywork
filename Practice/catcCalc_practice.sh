#!/bin/bash

# Author: Norbert Antal

# starting points of the solution
# simple calculator ref: https://www.geeksforgeeks.org/simple-calculator-bash/
# number table ref: https://www.geeksforgeeks.org/shell-script-to-print-table-of-a-given-number/
# working syntax for arithmetics ref: https://linuxconfig.org/bash-scripting-operators
# compare strings with if ref: https://linuxize.com/post/how-to-compare-strings-in-bash/

fncalculator()
{
# shellscript functions ref: https://www.shellscript.sh/functions.html
# operation selected with if function checking user imput stored in "operator"
# program than takes user imput stored in operand as first opernad and 
# generates the second operand with a for loop in a range 1-15 storing each iteration in 'i'
# program will repeat the operation with each iteration of i until reaching 15.

    i=1 #initialising loop
    clear
    echo "Number table of $operand $operator range of 1-15" # user interaction - output label
    #Addition
    if [[ "$operator" == "+" ]] #compare strings entered with and stored in "operator", if match, carry out while loop with operator, else jump to next
    then
        while [[ $i -ge 1 && $i -le 15 ]] # check if value is within range ref: https://stackoverflow.com/questions/50521798/how-to-check-if-a-number-is-within-a-range-in-shell        
        do
            echo "$operand + $i = $(($operand + $i))" # outputs first operand, operator, second operand (current iteration) and the result
            ((++i))
        done
    #Substraction
    elif [[ "$operator" == "-" ]]
    then
        while [[ $i -ge 1 && $i -le 15 ]]
        do
            echo "$operand - $i = $(($operand - $i))"
            ((++i))
        done
    #Multiplication
    elif [[ "$operator" == "*" ]]
    then
        while [[ $i -ge 1 && $i -le 15 ]]
        do
            echo "$operand * $i = $(($operand * $i))" 
            ((++i))
        done
    #Division    
    elif [[ "$operator" == "/" ]]
    then
        for i in {1..15}
        do
            #without bc installed shell script does not support floating point arithmetic ref: https://linuxhint.com/floating-point-math-bash/#:~:text=With%20the%20bc%20arbitrary%20precision,pipe%20in%20this%20bash%20file
            #echo "$operand / $i = $(($operand / $i))"
            echo "$operand / $i = $(echo "scale=4; $operand / $i" | bc | sed 's/^\./0./' )" #ref: https://stackoverflow.com/questions/8402181/how-do-i-get-bc1-to-print-the-leading-zero
            
        done
    #Exponentiation    
    elif [[ "$operator" == "^" ]]
    then
        for i in {1..15}
        do
            echo $operand ^ $i = $[ $operand ** $i ] 
        done
    else
        clear
        echo "Invalid operator entered. Program terminated - try running the program again..."
    fi
}
fnentryvalid()
{
    echo "Please enter operand within 1-15"
# check valid entry ref: https://stackoverflow.com/questions/50521798/how-to-check-if-a-number-is-within-a-range-in-shell
    read operand
    if (($operand >= 1 && $operand <= 15)); then
        fncalculator # using shellscript for
    else
        echo "Invalid input, number must be in range (1-15)."
        fnentryvalid # using shellscript to be able to use validation without the program exiting
fi
}

echo "Enter the symbol for the operation you want to perform:"
echo "Addition (+)"
echo "Subtraction (-)"
echo "Multiplication (*)"
echo "Division (/)"
echo "Exponent (^)"
read operator

echo "Please enter operand within 1-15"
# check valid entry ref: https://stackoverflow.com/questions/50521798/how-to-check-if-a-number-is-within-a-range-in-shell
read operand
if (($operand >= 1 && $operand <= 15)); then
    clear #clear the terminal
  fncalculator #use function so script easier to read
else
  echo "Invalid input, number must be in range (1-15)."
  fnentryvalid #reuse function without program exitin
fi