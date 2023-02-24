# Primes.py
# Author: Norbert Antal
# creating a list of primes

max = int(input("primes between 0 and: ")) # user input for max range
primes = [] #primes list container
for prime in range(2, max): # candidate numbers to be tested if they are prime
    for div in range(2, prime): # cycling divider number (starts with 2 and ends before the candidate)
        if prime%div == 0: # check if candidate divisible by div without remainder
            break # if yes, jump back to cycle the next divider within range or get the next prime candidate if range is filled
    else: #if not divisible, it IS a prime
        primes.append(prime) # so it can be added to the list of primes
print(*primes) # when prime candidate cycle finished, prints primes list