# i)
# type 1:
print("Type 1: \n ")
import math
from sympy import primefactors

num = [564, 101226,14,1523]

for n in num:
    print(f"{n}:{primefactors(n)}")

# type 2:
print("\nType 2:\n")

#function to find prime factors 
def prime_factors(n):
    factors =[] #store factors
    i = 2   #start with smallest prime number

    while i * i <= n: #check up to squre root of n
        if n % i == 0:  #chech if i devides n completely
            factors.append(i)# Add it to the list
            n //=i #Divide n by i (reduce the number)
        else:
            i += 1 # Try next number

    if n > 1:   
        factors.append(n) # Add the last remaining prime factor

    return factors

numbers = [564, 101226, 14, 1523]

for num in numbers:
    print(f"{num}:{prime_factors(num)}")


# ii)

import math

