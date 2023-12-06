# program that reads in two numbers and
# outputs the integer answer and remainder
x = int(input("first number: "))
y = int(input("second number: "))
result = int(x//y)
remains = x%y
print ("{} divided by {} is {} remains {}". format(x,y,result,remains))