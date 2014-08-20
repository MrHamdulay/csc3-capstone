# Dalise Steynfaard
# STYDAL001
# Assignment 3, question 4
# March 2014

import math

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
prime = True

for i in range(n+1,m):
    if str(i)[::-1] == str(i):
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if not(i==2) and i%j==0:
                prime = False
                break
            else:
                prime = True
        if prime:
            print(i)