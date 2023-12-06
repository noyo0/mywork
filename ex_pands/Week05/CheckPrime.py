# This checks if a number is priem or not

prime = int(input("check if this one is prime: "))
for div in range(2,prime):
    if prime % div == 0:
        IsPrime = False
        break
else:
    IsPrime = True
if IsPrime == True:
    print(f"yes {prime} is Prime")
else:
    print(f"no {prime} is not a Prime")